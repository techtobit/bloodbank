# class DonarListView(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.AllowAny]
#     def get(self, request, format=None):
#             users = User.objects.all()
#             serializer= DonarListSerializer(users, many=True)

#             return Response(serializer.data)
        
# class DonarProfileView(APIView):
#     # uthentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.AllowAny]
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#             user =self.get_object(pk=pk)
#             serializer= DonarProfileSerializer(user, many=False)
#             return Response(serializer.data)
#     def put(self, request, pk, format=None):
#         user =self.get_object(pk=pk)
#         serializer= DonarProfileSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     def delete(self, pk):
#         user =self.get_object(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)