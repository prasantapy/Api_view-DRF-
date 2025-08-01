from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Job_Profile
from rest_framework.response import Response
from api.Serializer import ProfileSerializer
from rest_framework.generics import ListAPIView,CreateAPIView ,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# approche 1 [APIView]
#class profile_view(APIView):
#    def get(self,request,*args,**kwargs):
#        qs=Job_Profile.objects.all()
#       serizations=ProfileSerializer(qs,many=True)

#        return Response(serizations.data)


# approche 2    [listAPIVIEW]

#class Profile_ListAPIView(ListAPIView):
              #queryset=Job_Profile.objects.all()
       #serializer_class=ProfileSerializer
       #def get_queryset(self):
        #      user_id=self.kwargs.get('id')
        #      if user_id:
        #            qs=Job_Profile.objects.filter(id=user_id)
        #            if not qs.exists():
        #                   from rest_framework.exceptions import NotFound
        #                   raise NotFound(detail=f"User with id={user_id} not found.")
                    
                            
        #      return qs
       
#class profile_Create_APIView(CreateAPIView):
#    queryset=Job_Profile.objects.all()
#    serializer_class=ProfileSerializer
    
#class profile_RetrieveAPIView(RetrieveAPIView):
#    queryset=Job_Profile.objects.all()
#    serializer_class=ProfileSerializer

       
class profile_UpdateAPIView(UpdateAPIView):
    queryset=Job_Profile.objects.all()
    serializer_class=ProfileSerializer
   
class profile_DestroyAPIView(DestroyAPIView):
    queryset=Job_Profile.objects.all()
    serializer_class=ProfileSerializer
    


            