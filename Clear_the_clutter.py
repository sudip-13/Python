import os
new_file_names = ["new_file1.pdf", "new_file2.pdf", "new_file3.pdf","4.pdf","5.pdf","6.pdf","7.pdf","8.pdf","9.pdf"]
def rename(ext):
    j=0
    fol=os.listdir("oscreation")
    for i in range(len(fol)):
        if(fol[i][-1]==ext[-1] and fol[i][-2]==ext[-2] and fol[i][-3]==ext[-3]):
            j+=1
            os.rename(f"oscreation/{fol[i]}",f"oscreation/{j}.{ext}")
rename("jpg")