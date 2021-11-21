from django.http.response import HttpResponse
from django.shortcuts import render ,HttpResponse
from django.core.files.storage import FileSystemStorage
from PyPDF2 import PdfFileWriter, PdfFileReader


# Create your views here.
def index(request):
    # return HttpResponse("Done")
    return render(request,"index.html")

def secure(request):
    # if request=='POST':
    myfile = request.FILES['pdfe']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    print("Yes")
    password=request.POST.get('password')
    print(password)
    file=request.POST.get('pdfe')
    print(file)
    print(filename)
    print(uploaded_file_url)
    from PyPDF2 import PdfFileWriter, PdfFileReader
    out = PdfFileWriter()
    file = PdfFileReader(f"media/{filename}")
    num = file.numPages
    for idx in range(num):
    	
	# Get the page at index idx
	    page = file.getPage(idx)
    
	    # Add it to the output file
	    out.addPage(page)
    out.encrypt(password)

# Open a new file "myfile_encrypted.pdf"
    with open(f"media/protect/{filename}", "wb") as f:
	
	# Write our encrypted PDF to this file
	    out.write(f)


        
        
        
    
    dic={
        'filename':filename,
        'password':password,
    }
    return render(request, 'secure.html',dic)