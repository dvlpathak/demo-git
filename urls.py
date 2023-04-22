from django.contrib import admin
from django.urls import path,include
from . import view
from django.conf import settings
from django.conf.urls.static import static
from digitaluser import views

urlpatterns = [
        
        path('admin/', view.loginform),
        path('', include('digitaluser.urls')),

        path('Index/', view.index),
        path('UserLogin/', view.UserLogin),
        path('Logout/', view.logoutUser),
        
        #------------ACM URLS-------------------------
        path('RoleACM/', view.openRoleACM),
        path('AddRoleACM/', view.addRoleACM),
        path('deleteRoleACM/', view.deleteRoleACM),
        
        path('EmployeeACM/', view.openEmployeeACM),
        path('AddEmployeeACM/', view.addEmpACM),
        path('PrivilegeACM/', view.openPrivilegeACM),
        path('AddPrivilegeACM/', view.addPrivilegeACM),
        path('deletePrivACM/', view.deletePrivACM),
        path('PrivComponentACM/', view.openPrivComponentACM),
        path('AddPrivComponentACM/', view.addPrivComponentACM),
        
        
        path('CompanyACM/', view.openCompanyACM),
        path('AddCompanyACM/', view.addCompanyACM),
        path('AssignPrivToRoleACM/', view.AssignPrivToRoleACM),
        path('AddprivToroleACM/', view.AddprivToroleACM),
        path('AssignPrivToUserACM/', view.AssignPrivToUserACM),
        path('AddprivTouserACM/', view.AddprivTouserACM),
        

        #------------LOCATION URLS--------------------
        path('stateLocation/', view.openState),
        path('AddState/', view.addState),
        path('cityLocation/', view.openCity),
        path('AddCity/', view.addCity),
        path('areaLocation/', view.openArea),
        path('AddArea/', view.addArea),

        #------------AJAX URLS----------------------------------
        path('getprivilageRole/', view.getprivilageRole),
        path('getuser/', view.getuser),
        path('getprivilageUser/', view.getprivilageUser),
        path('getcity/', view.getcity),
        path('getemi/', view.getemi), #Student Registration
        
        
        path('AjaxForm/', view.AjaxForm),
        path('addajax/', view.addajax),
        path('getAjaxData/', view.getAjaxData),

        #------------MASTER URLS START------------------------
        path('Institute/', view.Institute),
        path('AddInstitute/', view.AddInstitute),
        path('ProgLanguage/', view.progLanguage),
        path('addProgLanguage/', view.addProgLanguage),
        path('FeesType/', view.FeesType),
        path('addFeesType/', view.addFeesType),
        path('FeesStructure/', view.FeesStructure),
        path('addFeesStructure/', view.addFeesStructure),
        path('StuBatch/', view.StuBatch),
        path('addStuBatch/', view.addStuBatch),
        path('BatchAllocation/', view.BatchAllocation),
        path('addInstallment/', view.addInstallment),
        
        #------------MASTER URLS END------------------------

        path('StuInquiry/', view.StuInquiry),
        path('AddStudentInquiry/', view.AddStudentInquiry),
        
        path('ConfirmStatus/', view.ConfirmStatus),
        path('RegisteredStatus/', view.RegisteredStatus),

        path('studentregistration/', view.studentregistration),
        path('RegisteredStudents/', view.registeredStudents),
        path('NextFollowup/', view.NextFollowup),
        path('cancelRemarks/', view.cancelRemarks),
        path('stuBatchAllocation/', view.stuBatchAllocation),        
        path('sendMssg/', view.sendMssg),
       
       path('dummyone/', view.dummyone),
       path('dummytwo/', view.dummytwo),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)