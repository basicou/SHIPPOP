import tkinter
from tkinter import ttk

def on_click():
    listsplit = list.get().split(',')
    searchmethod = method.get()
    searchvalue = int(search.get())

    #Change from string to integer
    i = 0
    while i < len(listsplit):
        listsplit[i] = int(listsplit[i])
        i = i + 1

    #Linear Search
    if searchmethod == '1. Linear Search':
        i = 0
        a = 0
        while i < len(listsplit):
            if searchvalue == listsplit[i]:
                announce = ('Round ' + str(i + 1) + ' ===> ' + str(searchvalue) + ' == ' + str(listsplit[i]) + ' found!!')
                tkinter.Label(test1, text=announce).grid(row=i + 3, column=1, padx=5, pady=5)
                a = a + 1
                break
            else :
                announce = ('Round ' + str(i + 1) + ' ===> ' + str(searchvalue) + ' != ' + str(listsplit[i]))
                tkinter.Label(test1, text=announce).grid(row=i + 3, column=1, padx=5, pady=5)
                a = a + 1
            i = i + 1

    #Binary Search
    elif searchmethod == '2. Binary Search':
        listsplit.sort()
        i = 0
        a = 0
        maxval = max(listsplit)
        minval = min(listsplit)
        mid = round((listsplit.index(maxval)-listsplit.index(minval))/2)
        while i < len(listsplit):
            if searchvalue == listsplit[mid]:
                announce = ('Round ' + str(i + 1) + ' ===> ' + str(searchvalue) + ' == ' + str(listsplit[mid]) + ' found!!')
                tkinter.Label(test1, text=announce).grid(row=i + 3, column=1, padx=5, pady=5)
                a = a + 1
                break
            else :
                announce = ('Round ' + str(i + 1) + ' ===> ' + str(searchvalue) + ' != ' + str(listsplit[mid]))
                tkinter.Label(test1, text=announce).grid(row=i + 3, column=1, padx=5, pady=5)
                a = a + 1
                if searchvalue > int(listsplit[mid]):
                    minval = listsplit[mid]
                    mid = round((listsplit.index(maxval) + listsplit.index(minval))/2)
                else :
                    maxval = listsplit[mid]
                    mid = round((listsplit.index(maxval) - listsplit.index(minval))/2)
            i = i + 1

    #Bubble Search
    if searchmethod == '3. Bubble Search':
        i = 0
        a = 0
        while i < len(listsplit):
            if searchvalue == listsplit[i]:
                announce = ('Round ' + str(i + 1) + ' ===> ' + str(searchvalue) + ' == ' + str(listsplit[i]) + ' found!!')
                tkinter.Label(test1, text=announce).grid(row=i + 3, column=1, padx=5, pady=5)
                a = a + 1
                break
            else :
                announce = ('Round ' + str(i + 1) + ' ===> ' + str(searchvalue) + ' != ' + str(listsplit[i]))
                tkinter.Label(test1, text=announce).grid(row=i + 3, column=1, padx=5, pady=5)
                a = a + 1
            i = i + 1

test1 = tkinter.Tk()

test1.option_add('*font', 'consola 10')
test1.title('Shippop_Test_Div1')

#Get List Data
tkinter.Label(test1,text='List : ').grid(row = 0, column = 0, padx = 5, pady=5)
list = tkinter.Entry(test1, width = 50)
list.grid(row = 0, column = 1, padx = 5, pady=5)

#Select Method which use for search the number
tkinter.Label(test1,text='method : ').grid(row = 1, column = 0, padx = 5, pady=5)
method = ttk.Combobox(test1, values=['1. Linear Search','2. Binary Search','3. Bubble Search'], width = 50)
method.grid(row = 1, column = 1, padx = 5, pady=5)

#Input the number that want to search
tkinter.Label(test1,text='Search : ').grid(row = 2,column = 0,padx = 5, pady=5)
search = tkinter.Entry(test1, width = 15)
search.grid(row = 2,column = 1, padx = 5, pady=5)
click_search = tkinter.Button(test1, text='Search', command = on_click)
click_search.grid(row = 2, column = 2, padx = 5, pady=5)

#Result Role
tkinter.Label(test1,text='Result : ').grid(row = 3,column = 0, padx = 5, pady=5)

test1.mainloop()
