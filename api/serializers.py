from rest_framework import serializers
from .models import Student
    
# In this serializer class we dont have to add fields and create update functions manually.


class StudentSerializer(serializers.ModelSerializer):

# Custom Validator if we write manual serializer class
def c_valid(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with r')
name = serializers.CharField(validators=[c_valid])
#    name = serializers.CharField(read_only=True)              # If we want to put an argument in one specific field thats how we will do


    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name','roll']                    #If we want to put an argument in multiple field
        extra_kwargs = {'name':{'read_only':True}}              #Another way but in this way we can pass other arguments too 
#        fields = ['name','roll','city']                        # We can write like this also means all mentioned fields
#        exclude = ['city']                                     # exclude mean all fields except the city


    # # Field Level Validation (For validating single field we will use this)
    # def validate_roll(self, value):       # VALIDATE IS KEYWORD AND with it we will write field name we want to validate
    #     if value >= 200:
    #         raise serializers.ValidationError('Seats are full')
    #     return value


    # Object Level Validation (If we want to validate more than one field we will use this)
    def validate(self, data):
        # We have all fields data in data parameter so we will get the fields we want to validate
        nm = data.get('name')
        ct = data.get('city')
        if nm == 'ahmad' and ct == 'lahore':
            raise serializers.ValidationError('Data vot valid')
        return data










    #       Manuall serializer class

# Custom Validator if we write manual serializer class
# def c_valid(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should start with r')


# class StudentSerializer(serializers.Serializer):

#     name = serializers.CharField(max_length=100, validators=[c_valid])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)


#     # For creating new data in Database through API (Front-end)
#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)


#     # For updating data through Api (Front-end)
#     def update(self, instance, validate_data):
#         print(instance.name)
#         instance.name = validate_data.get('name', instance.name)
#         print(instance.name)
#         instance.roll = validate_data.get('roll', instance.roll)
#         instance.city = validate_data.get('city', instance.city)
#         instance.save()
#         return instance




    # Field Level Validation (For validating single field we will use this)
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seats are full')
    #     return value
    

    # # Object Level Validation (If we want to validate more than one field we will use this)
    # def validate(self, data):
    #     # We have all fields data in data parameter so we will get the fields we want to validate
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'ahmad' and ct.lower() != 'lahore':
    #         raise serializers.ValidationError('Data vot valid')
    #     return data


