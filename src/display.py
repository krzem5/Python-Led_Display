import atexit
import numpy as np
import rpi_ws281x as ws



def _map_pos(x,y,sz):
	return (x if y%2==0 else sz[0]-x-1)+y*sz[0]



def color(r=255,g=None,b=None):
	if (g is None):
		g=b=r
	return (r<<16)|(g<<8)|b



class LED_Data(object):
	def __init__(self,ch,sz):
		self.sz=sz
		self.ch=ch



	def __getitem__(self,i):
		if (isinstance(i,slice)):
			return [ws.ws2811_led_get(self.ch,n) for n in range(*i.indices(self.sz[0]*self.sz[1]))]
		if (isinstance(i,tuple)):
			i=_map_pos(i[0],i[1],self.sz)
		return ws.ws2811_led_get(self.ch,i+self.sz[0]*self.sz[1])



	def __setitem__(self,i,v):
		if (isinstance(i,tuple)):
			i=_map_pos(i[0],i[1],self.sz)
		if (isinstance(i,slice)):
			j=0
			for n in range(*i.indices(self.sz)):
				ws.ws2811_led_set(self.ch,n,color(*v[j]))
				j+=1
		return ws.ws2811_led_set(self.ch,i,color(*v))



	def image(self,img):
		a=np.asarray(img.convert("RGB"))
		xr=int(a.shape[1]/self.sz[0])
		yr=int(a.shape[0]/self.sz[1])
		for i in range(0,self.sz[0]):
			for j in range(0,self.sz[1]):
				s=[0,0,0]
				for k in range(i*xr,i*xr+xr):
					for l in range(j*yr,j*yr+yr):
						s[0]+=a[l,k,0]
						s[1]+=a[l,k,1]
						s[2]+=a[l,k,2]
				self.__setitem__((i,j),(int(s[0]/(xr*yr)),int(s[1]/(xr*yr)),int(s[2]/(xr*yr))))



class Display(object):
	def __init__(self,leds=[32,8],pin=18,channel=0,freq_hz=800000,dma=5,invert=False,brightness=255,type_=ws.WS2811_STRIP_GRB):
		self._leds=ws.new_ws2811_t()
		for cn in range(2):
			c=ws.ws2811_channel_get(self._leds,cn)
			ws.ws2811_channel_t_count_set(c,0)
			ws.ws2811_channel_t_gpionum_set(c,0)
			ws.ws2811_channel_t_invert_set(c,0)
			ws.ws2811_channel_t_brightness_set(c,0)
		self._ch=ws.ws2811_channel_get(self._leds,channel)
		ws.ws2811_channel_t_count_set(self._ch,leds[0]*leds[1])
		ws.ws2811_channel_t_gpionum_set(self._ch,pin)
		ws.ws2811_channel_t_invert_set(self._ch,(0 if invert==False else 1))
		ws.ws2811_channel_t_brightness_set(self._ch,brightness)
		ws.ws2811_channel_t_strip_type_set(self._ch,type_)
		ws.ws2811_t_freq_set(self._leds,freq_hz)
		ws.ws2811_t_dmanum_set(self._leds,dma)
		self.data=LED_Data(self._ch,leds)
		atexit.register(self._c)
		r=ws.ws2811_init(self._leds)
		if (r!=ws.WS2811_SUCCESS):
			raise RuntimeError(ws.ws2811_get_return_t_str(r))



	def brightness(self,b):
		ws.ws2811_channel_t_brightness_set(self._ch,b)



	def run(self,f,*a,**kw):
		try:
			f(self,*a,**kw)
		except KeyboardInterrupt:
			self._c()



	def update(self):
		r=ws.ws2811_render(self._leds)
		if (r!=ws.WS2811_SUCCESS):
			raise RuntimeError(ws.ws2811_get_return_t_str(r))



	def _c(self):
		for i in range(self.data.sz[0]*self.data.sz[1]):
			ws.ws2811_led_set(self.data.ch,i,0)
		ws.ws2811_render(self._leds)
		ws.delete_ws2811_t(self._leds)
