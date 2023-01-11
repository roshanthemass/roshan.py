library(wrapr)
name <- c("anastasia","dima","katherine","'james","emily","michael","mathew","laura","kevin","jonas")
score <-c(12.5,9,16.5,12,9,20,14.5,13.5,8,19)
attempts <- c(1,3,2,3,2,3,1,1,2,1)
qualify <- c("yes","no","yes","no","no","yes","yes","no","no","yes")
data1 <-data.frame(name,score,attempts,qualify)
print(data1)

print("extract is")
extract<-data1[c(3,5),c(1,3)]
print(extract)

aggregate(score~attempts,data1,mean)

list1=list(name,score,attempts,qualify)
print(list1)

converted= as.data.frame(do.call(cbind,list1))
print(converted)

a=matrix(c(1,1,1,2,2,2,3,3,3),ncol = 3)
print(a)
b=matrix(c(1,2,3,2,3,1,3,2,1),ncol = 3)
print(b)
print(a+b)

a=matrix(c(1,1,1,2,2,2,3,3,3),ncol = 3)
c <- matrix(a, nrow = 3, ncol = 3)
d <- t(c)
print(d)