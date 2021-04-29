import os



print('----------------------------------------------------------')
print('Dizin Tarama Programıdır EmreZeriX Tarafından Kodlanmıştır')
print('----------------------------------------------------------')
print('1-Dirsearch İle tara(Yakında gelicek kullanmayın!)')
print('2-Dirb İle tara')
print('3-GoBuster İle tara')
print('----------------------------------------------------------')
a = input('Hangi Aracı kullanmak istiyorsunuz:')

if(a=='1'):
    q = input('Dirsearch sistemde kurulu mu?(e/h)')
    if(q=='e'):
        print('Dirsearch İle Devam Ediliyor!')
        b = input('Hedef Site:')
        c = input('Taram istediğiniz Uzantı Türü:')
        os.system('python3 dirsearch -u {0} -e {1}'.format(b,c))
    if(q=='h'):
        print('Dirsearch kuruluyor...')
        os.system('git clone https://github.com/maurosoria/dirsearch')
        print('Dirsearch kuruldu.')
        ö = input('Devam etmek istiyormusunuz(e/h):')
        if(ö=='e'):
               print('Dirsearch İle Devam Ediliyor!')
               b = input('Hedef Site:')
               c = input('Taram istediğiniz Uzantı Türü:')
               os.system('cd dirsearch')
               os.system('python3 dirsearch -u {0} -e {1}'.format(b,c))
        if(ö=='h'):
            breakpoint
        else:
            print('e yada h yazman gerek!')
    else:
        print('e yada h yazman gerek')
if(a=='2'):
    print('Dirb Aracı ile devam ediliyor...')
    d = input('Hedef site:')
    print('-------------------------------')
    print('1-big.txt')
    print('2-catala.txt')
    print('3-common.txt')
    print('4-euskera.txt')
    print('5-extensions_common.txt')
    print('6-indexes.txt')
    print('7-mutations_common.txt')
    print('8-small.txt')
    print('9-spanish.txt')
    print('-------------------------------')
    z = input('Hangi Wordlisti kullanmak istiyorsunuz:')
    if(z=='1'):
            os.system('dirb {0} /usr/share/dirb/wordlists/big.txt'.format(d))
    if(z=='2'):
        os.system('dirb {0} /usr/share/dirb/wordlists/catala.txt'.format(d))
    if(z=='3'):
        os.system('dirb {0} /usr/share/dirb/wordlists/common.txt'.format(d))
    if(z=='4'):
        os.system('dirb {0} /usr/share/dirb/wordlists/euskera.txt'.format(d))
    if(z=='5'):
        os.system('dirb {0} /usr/share/dirb/wordlists/extensions_common.txt'.format(d))
    if(z=='6'):
        os.system('dirb {0} /usr/share/dirb/wordlists/indexes.txt'.format(d))
    if(z=='7'):
        os.system('dirb {0} /usr/share/dirb/wordlists/mutations_common.txt'.format(d))
    if(z=='8'):
        os.system('dirb {0} /usr/share/dirb/wordlists/small.txt'.format(d))
    if(z=='9'):
        os.system('dirb {0} /usr/share/dirb/wordlists/spanish.txt'.format(d))
    else:
        print('Yanlış wordlist seçtiniz!')                                
if(a=='3'):
    print('GoBuster İle Devam ediliyor..')
    e = input('Hedef Site:')
    print('-------------------------------')
    print('1-big.txt')
    print('2-catala.txt')
    print('3-common.txt')
    print('4-euskera.txt')
    print('5-extensions_common.txt')
    print('6-indexes.txt')
    print('7-mutations_common.txt')
    print('8-small.txt')
    print('9-spanish.txt')
    print('-------------------------------')
    z = input('Hangi Wordlisti kullanmak istiyorsunuz:')
    if(z=='1'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/big.txt'.format(e))
    if(z=='2'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/catala.txt'.format(e))
    if(z=='3'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/common.txt'.format(e))
    if(z=='4'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/euskera.txt'.format(e))
    if(z=='5'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/extensions_common.txt'.format(e))
    if(z=='6'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/indexes.txt'.format(e))
    if(z=='7'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/mutations_common.txt'.format(e))
    if(z=='8'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/small.txt'.format(e))
    if(z=='9'):
        os.system('gobuster dir -u {0} -w /usr/share/dirb/wordlists/spanish.txt'.format(e))
    else:
        print('Wordlist seçmediniz!')
else:
    print('Araç seçmedin demekki kullanmak istemiyorsun :/')                            
