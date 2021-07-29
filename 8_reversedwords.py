def reverse_words(s):
        print(s)
        a = ''
        a = s.split(" ")
        reverse = ''
        for i in range(len(a)-1,-1,-1):
            reverse+= a[i] + ' ' 
            print(str(reverse))
        return reverse
   
