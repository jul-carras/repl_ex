def update_w_and_b(x,y,w,b,alpha):
  dl_dw =0.0
  dl_db=0.0
  N=len(x)
  for i in range(N):
    dl_dw += -2*x[i]*(y[i]-(w*x[i]+b))
    dl_db += -2*(y[i]-(w*x[i]+b))
  
  w = w-(1/float(N))*dl_dw*alpha
  b = b-(1/float(N))*dl_db*alpha
  return w,b
def train(x,y,w,b,alpha,epochs):
  for e in range(epochs):
    w,b = update_w_and_b(x,y,w,b,alpha)
    if e%400 ==0:
      print("epoch:",e, w,b )
  return w,b 
def predict(x,w,b):
  return w*x+b

x=[0,1,2,3,4,5,6,7,8,9]
y=[0,2,4,6,8,10,12,14,16,18]

w,b = train(x,y,0.0,0.0,0.001,20000)
x_new =12
y_new = predict(x_new,w,b)
print(y_new)

