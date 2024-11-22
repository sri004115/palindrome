from django.shortcuts import render

# View for the input form
def index(request):
    return render(request, 'index.html')

# View to check if the number is palindrome
def check_palindrome(request):
    if request.method == "POST":
        number = request.POST.get('num')
        
        # Check if number is a palindrome
        is_palindrome = number == number[::-1]  # Reverse the string and compare
        
        return render(request, 'index2.html', {'is_palindrome': is_palindrome, 'number': number})
    return render(request, 'index.html')
"""
perform the below 
initialize a git respository in an existing project directory.
add a file to the staging area .
create a feature branch ,make changes and merge it into the main branch.
commit changes with a meaningful commit message

"""