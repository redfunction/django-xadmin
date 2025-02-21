from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

SERVER_STATUS = (
    (0, "Normal"),
    (1, "Down"),
    (2, "No Connect"),
    (3, "Error"),
)
SERVICE_TYPES = (
    ('moniter', "Moniter"),
    ('lvs', "LVS"),
    ('db', "Database"),
    ('analysis', "Analysis"),
    ('admin', "Admin"),
    ('storge', "Storge"),
    ('web', "WEB"),
    ('email', "Email"),
    ('mix', "Mix"),
)


class IDC(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    contact = models.CharField(max_length=32)
    telphone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    is_valid = models.BooleanField(default=False)
    customer_id = models.CharField(max_length=128)
    groups = models.ManyToManyField(Group)  # many

    create_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "IDC"
        verbose_name_plural = verbose_name


class Host(models.Model):
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    nagios_name = models.CharField("Nagios Host ID", max_length=64, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    internal_ip = models.GenericIPAddressField(blank=True, null=True)
    user = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    ssh_port = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(choices=SERVER_STATUS)

    brand = models.CharField(max_length=64, choices=[(i, i) for i in ("DELL", "HP", "Other")])
    model = models.CharField(max_length=64)
    cpu = models.CharField(max_length=64)
    core_num = models.SmallIntegerField(choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)])
    hard_disk = models.IntegerField()
    memory = models.IntegerField()

    system = models.CharField("System OS", max_length=32, choices=[(i, i) for i in ("CentOS", "FreeBSD", "Ubuntu")])
    system_version = models.CharField(max_length=32)
    system_arch = models.CharField(max_length=32, choices=[(i, i) for i in ("x86_64", "i386")])

    create_time = models.DateField()
    guarantee_date = models.DateField()
    service_type = models.CharField(max_length=32, choices=SERVICE_TYPES)
    description = models.TextField()

    administrator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Admin")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Host"
        verbose_name_plural = verbose_name


class MaintainLog(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()

    def __str__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type, self.hard_type)

    class Meta:
        verbose_name = "Maintain Log"
        verbose_name_plural = verbose_name


class HostGroup(models.Model):

    name = models.CharField(max_length=32)
    description = models.TextField()
    hosts = models.ManyToManyField(
        Host, verbose_name=u'Hosts', blank=True, related_name='groups')

    class Meta:
        verbose_name = "Host Group"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    date = models.DateField()
    user_count = models.IntegerField()
    view_count = models.IntegerField()

    class Meta:
        verbose_name = "Access Record"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s Access Record" % self.date.strftime('%Y-%m-%d')
