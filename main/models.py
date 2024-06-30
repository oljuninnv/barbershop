from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50,help_text='Введите имя работника',verbose_name="Имя")
    lastname = models.CharField(max_length=50,null=True,blank=True,help_text='Введите отчество работника',verbose_name="Отчество")
    surname = models.CharField(max_length=50,help_text='Введите фамилию работника',verbose_name="Фамилия")
    photo = models.ImageField(upload_to='worker_photos',help_text='Загрузите фото работника',verbose_name="Фото",null=True,blank=True)
    work_experience = models.IntegerField(help_text='Введите рабочий опыт работника',verbose_name="Опыт работы")
    phone = models.CharField(max_length=12,help_text='Введите номер работника',verbose_name="Мобильный телефон")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at','work_experience']
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        
    def __str__(self) -> str:
        return f'{self.name + " " + self.surname}'

class Service(models.Model):
    name = models.CharField(max_length=100,help_text='Введите название услуги',verbose_name="Название услуги")
    price = models.DecimalField(max_digits=8, decimal_places=2,help_text='Введите стоимость услуги',verbose_name="Цена")
    
    class Meta:
        ordering = ['name','price']
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    
    def get_service(self): return ",".join([str(p) for p in self.Service.all()])

    def __str__(self) -> str:
        return f'{self.name} - {self.price}'
    
class Visiting(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,verbose_name="Работник",null=False)
    service = models.ManyToManyField (Service,verbose_name="Услуга",null=True,blank=True)
    customer_name = models.CharField(max_length=100,verbose_name="Имя",null=True,blank=True)
    customer_phone = models.CharField(max_length=12,verbose_name="Мобильный телефон",null=True,blank=True)
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время",null=True,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="Итоговая цена",null=True,blank=True)

    class Meta:
        ordering = ['date','time','worker']
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self)-> str:
        return f'{self.worker.name,self.worker.surname,self.customer_name,self.service,self.date,self.time,self.price}'