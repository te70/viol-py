import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]

    dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print('found password:' +word)
            return
    print ("Password not found")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("cracking passsword for" +user)
            testPass(cryptPass)

if __name__ == '__main__':
    main() 