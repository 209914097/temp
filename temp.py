clear clc
warning off
for a=0:0.1:18
    x=-1.8:0.001:1.8;
    y=x.^(2/3)+0.9*abs((3.3-x.^2)).^(1/2).*sin(a*pi*x);
    y(1:1800)=-y(1:1800);  
    plot(x,y,'r');   
    axis([-2,2,-2,2.5])
    pause(0.05)
end
warning on
