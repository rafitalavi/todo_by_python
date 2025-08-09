from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Role
from .forms import RoleForm

@login_required 
def roleindex(request):
    roles = Role.objects.all().order_by('id')
    
    # Always define form before checking POST
    form = RoleForm()

    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roleapp:roleindex')

    return render(request, 'roleapp/rolelist.html', {
        'roles': roles,
        'form': form,
    })
from django.shortcuts import get_object_or_404

@login_required
def role_edit(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('roleapp:roleindex')
    else:
        form = RoleForm(instance=role)

    return render(request, 'roleapp/role_edit.html', {
        'form': form,
        'role': role,
    })
   
