password_dictionary = 
{
	'0':'rly', '1':'!p', '2':'px', '3':'@x', '4':'&g', '5':'#z', 
	'6':'?x', '7':'lz', '8':'y5','9':'fn','a':'$2','A':'%1','b':'2a','B':'1x','c':'3X',
	'C':'6s','d':'!2', 'D':'6z','e':'Ax','E':'2!','f':'4g','F':'3g','g':'ax','G':'1@',
	'h':'H','H':'p!','i':'i','I':'i','j':'4$','J':'R1','k':'R2','K':'z#','l':'<1',
	'L':'>$','m':'fe','M':'ce','n':'zq','N': 'ep', 'o':'tr','O':'xs','p':'<t','P':'>r',
	'q': 'yz', 'Q':'E3', 'r':'f4','R':'%1','s':'$3','S':'#0','t':'mib','T':'4!','u':'.o',
	'U':'v3', 'v':'z.', 'V':'k#', 'w':'3#','W':'>i', 'y':'b4','Y':'n7', 'z':'m4','Z':'s2'
}
  
def crypto(password):
  count = 0
  new_pass = []
  pass_len = len(password)
  while count < pass_len:
    new_pass.append(password_dictionary[password[count]])
    count+=1
  return "".join(new_pass)
  
inp_pass = input('Enter a password (only numbers):')
print('Your new pass is:')
print(crypto(inp_pass))
