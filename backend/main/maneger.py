from django.contrib.auth.models import BaseUserManager

class ManagerCustomUser(BaseUserManager):
    
    def create_user(self, email, password, registrationNumber, **extra_fields):
        
        if not email:
            raise ValueError("Invalid e-mail!")
        if not registrationNumber: 
            raise ValueError("Invalid registrationNumber!")
         
        email = self.normalize_email(email)
        user= self.model(email=email, registrationNumber=registrationNumber, 
                         **extra_fields)
        
        user.set_password(password)
        user.save()
        return user 
        
    
    def create_superuser(self, email, passaword ,registrationNumber, **extra_fields):
        
        user = self.create_user(
            email,
            passaword=passaword,
            registrationNumber=registrationNumber
            
        )
        user.save(using=self._db)
        return user