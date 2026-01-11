# /b coincide con el principio o final de una palabra 

import re 
text = "casa coche perro acasa casado casada "

pattern = r"casa"

found = re.findall(pattern, text)

print(found)