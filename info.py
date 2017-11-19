from os import *

def main():
	path = '/sys/module/rt2800pci/sections/'
	chdir(path)
	section = popen('ls .*').read()
	section =  section.split('\n')
	section = section[:section.index('')]
#	print section

	addr = popen('cat .*').read()
	addr = addr.split('\n')
	addr = addr[:-1]
#	print addr

	if len(section) != len(addr):
		print 'Something wrong!'
		return

	payload = addr[section.index('.text')] + ' '

	for i in range(len(section)):
		if i==section.index('.text'):
			continue
		payload += '-s '
		payload += section[i] + ' '
		payload += addr[i] + ' '

	print payload

main()