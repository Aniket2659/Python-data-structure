def formatted_text(string,width):
    words=string.split()
    # text=' '.join(words)
    para=''
    para_len=0
    for j in words:
        if para_len+len(j)<=width:
            para=para+j+" "
            para_len=para_len+len(j)
        else:
            para=para+'\n'+j+""
            para_len=len(j)+1

    return para
string="""Before executing code, Python interpreter reads source file and define few special variables/global variables. If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable."""
print(formatted_text(string,50))

