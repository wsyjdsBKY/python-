#coding=utf-8
from multiprocessing import Pool,Manager
import os
def cpfile(name,newfilename,oldfilename):
	#完成对文件的拷贝
	print(name)
	fr = open(oldfilename+"/"+name)
	fw = open(newfilename+"/"+name,'w')
	print('---------')
	content = fr.read()
	fw.write(content)

	fr.close()
	fw.close()
	q.put(name)

def main():
	#0-获取要copy的文件夹的名字
	oldfilename = input('请输入要复制的文件夹的名字:')
	#1-创建一个新的文件夹
	newfilename = oldfilename+'-附件'
	os.mkdir(newfilename)
	#2-获取oldfilename中的所有文件的名字
	filenames = os.listdir(oldfilename)
	#3-使用多进程的方式copy源文件中的所有文件到新文件中去
	pool = Pool(5)
	queue = Manager.Queue()

	for name in filenames:
		pool.apply_async(cpfile,(name,newfilename,oldfilename，queue))
	num = 0
	allnums = len(filenames)
	while True:
		queue.get()
		num+=1
		copyRate = num/allnums
		print("\rcopy的进度是：%.2f%%"%(copyRate*100),end='')
	pool.close()
	pool.join()
if __name__ == "__main__":
	main()
print('ws')