import sys

# Thanks for the guy on /r/pcj making this and me smashing in
# command line arguments because I am lazy.
# I am perfectly capable of maintaining python 2 myself.
s="Test"

if len(sys.argv) < 2:
	print "argv[1] -> Input String"
else :
	s = sys.argv[1]	

l=len(s)
p=lambda n:[' 'for _ in range(n)]
print'    '+'\n    '.join([' '.join(s)]+
[' '.join([s[i]]+p(l-2)+[s[-i-1]]+p(i-1)+[s[-i-1]])for i in range(1,l-1)]+
[' '.join(list(s)[::-1]+p(l-2)+[s[0]])]+
[' '.join(p(i)+[s[-i-1]]+p(l-2)+[s[i]]+p(l-2-i)+[s[i]])for i in range(1,l-1)]+
[' '.join(p(i+1)+list(s))])
