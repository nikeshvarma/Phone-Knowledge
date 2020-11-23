from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class CarouselPhotos(models.Model):
    image_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, upload_to='slider_images/')

    def save(self, **kwargs):
        if not self.id and not self.image:
            return
        super(CarouselPhotos, self).save()

        image = Image.open(self.image)
        size = (1400, 800)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'Slider Photo'


class Mobile(models.Model):
    RAM_TYPES = [
        ('LPDDR3', 'LPDDR3'),
        ('LPDDR4', 'LPDDR4'),
        ('LPDDR4x', 'LPDDR4x'),
        ('LPDDR5', 'LPDDR5'),
    ]

    BUILD_TYPES = [
        ('Plastic Back', 'Plastic Back'),
        ('Glass Back', 'Glass Back'),
        ('Leather', 'Leather'),
        ('Other', 'Other'),
    ]

    DISPLAY_TYPES = [
        ('LCD', 'LCD'),
        ('IPS', 'IPS'),
        ('AMOLED', 'AMOLED'),
        ('S-AMOLED', 'S-AMOLED'),
        ('OLED', 'OLED'),
        ('RATINA', 'RATINA'),
    ]

    REFRESH_RATE = [
        ('60', '60 HZ'),
        ('90', '90 HZ'),
        ('120', '120 HZ'),
        ('144', '144 HZ'),
    ]

    PROTECTION_TYPE = [
        ('Gorila Glass 3', 'Gorila Glass 3'),
        ('Gorila Glass 4', 'Gorila Glass 4'),
        ('Gorila Glass 5', 'Gorila Glass 5'),
        ('Gorila Glass 6', 'Gorila Glass 6'),
    ]

    ANDROID_VERSION = [
        ('No', 'No'),
        ('Android 8.0', 'Android 8.0'),
        ('Android 9.0', 'Android 9.0'),
        ('Android 10.0', 'Android 10.0'),
        ('Android 11.0', 'Android 11.0'),
    ]

    IOS_VERSION = [
        ('10', '10'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('No IOS', 'No IOS'),
    ]

    SIM_TYPE = [
        ('Single Sim', 'Single Sim'),
        ('Dual Sim', 'Dual Sim'),
        ('Dual Sim with e-sim', 'Dual Sim with e-sim'),
        ('e-sim', 'e-sim'),
    ]

    BLUETOOTH_TECH = [
        ('4', 'Bluetooth 4'),
        ('4.1', 'Bluetooth 4.1'),
        ('4.2', 'Bluetooth 4.2'),
        ('5', 'Bluetooth 5'),
        ('5.1', 'Bluetooth 5.1'),
        ('5.2', 'Bluetooth 5.2'),
    ]

    STORAGE_TYPE = [
        ('eMMC 5.1', 'eMMC 5.1'),
        ('UFS 2.0', 'UFS 2.0'),
        ('UFS 2.1', 'UFS 2.1'),
        ('UFS 3.0', 'UFS 3.0'),
        ('UFS 3.1', 'UFS 3.1'),
    ]

    BATTERY_TYPE = [
        ('Li-ion', 'Li-ion'),
        ('Li-poly', 'Li-poly'),
    ]

    FINGERPRINT = [
        ('IN-Display', 'IN-Display'),
        ('Side Mounted', 'Side Mounted'),
        ('Rear Mounted', 'Rear Mounted'),
        ('No Fingerprint Sensor', 'No Fingerprint Sensor'),
    ]

    PHONE_TYPE = [
        ('Android', 'Android'),
        ('iPhone', 'iPhone'),
        ('Feature Phone', 'Feature Phone'),
        ('Tablet', 'Tablet')
    ]

    SPEAKER = [
        ('Single Speaker', 'Single Speaker'),
        ('Dual Speaker', 'Dual Speaker'),
    ]

    AUDIO_JACK = [
        ('3.5 mm Audio Jack', '3.5 mm Audio Jack'),
        ('Type C output', 'Type C Output'),
        ('No Jack Available', 'No Jack Available'),
    ]

    CHARGING_PORT = [
        ('Type C', 'Type C'),
        ('Micro USB', 'Micro USB'),
        ('Lighting', 'Lighting'),
    ]

    phone_type = models.CharField(max_length=100, choices=PHONE_TYPE)
    home_page_photo = models.ImageField(upload_to='phone_home_photos/')
    base_model_RAM = models.IntegerField(default=4)
    # Brand Details
    brand = models.CharField(max_length=200)
    phone_name = models.CharField(max_length=200)
    phone_variants = models.TextField()
    model_name = models.CharField(max_length=200, null=True)
    launch_date = models.DateField(null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    # Body dimension
    dimensions = models.CharField(max_length=200, null=True)
    weight = models.FloatField(null=True)
    build = models.CharField(choices=BUILD_TYPES, max_length=100)
    # display
    display_type = models.CharField(choices=DISPLAY_TYPES, max_length=100)
    display_size = models.CharField(max_length=200)
    display_refresh_rate = models.CharField(choices=REFRESH_RATE, max_length=100)
    display_resolution = models.CharField(max_length=200)
    display_protection = models.CharField(choices=PROTECTION_TYPE, max_length=150)
    HDR_support = models.BooleanField(default=True)
    # Platform
    UI_name = models.CharField(max_length=200)
    android_version = models.CharField(choices=ANDROID_VERSION, max_length=150)
    ios_version = models.CharField(max_length=100, choices=IOS_VERSION)
    processor = models.CharField(max_length=200)
    gpu = models.CharField(max_length=200, null=True)
    # Network
    network_technology = models.CharField(max_length=200, null=True)
    SIM_Type = models.CharField(choices=SIM_TYPE, max_length=150)
    wifi_technology = models.CharField(max_length=200, null=True)
    bluetooth = models.CharField(choices=BLUETOOTH_TECH, max_length=100)
    GPS = models.CharField(max_length=200, null=True)
    radio = models.BooleanField(default=True)
    NFC = models.BooleanField(default=False)
    # Memory
    RAM_Type = models.CharField(choices=RAM_TYPES, max_length=50)
    expandable_storage = models.BooleanField()
    storage_type = models.CharField(choices=STORAGE_TYPE, max_length=100)
    # Back Camera
    back_camera_setup = models.CharField(max_length=190)
    back_camera_resolution = models.TextField(blank=True)
    back_camera_features = models.TextField(blank=True)
    back_camera_video_features = models.TextField(blank=True)
    back_camera_flash = models.BooleanField()
    # Front Camera
    front_camera_setup = models.CharField(max_length=190)
    front_camera_resolution = models.TextField(blank=True)
    front_camera_features = models.TextField(blank=True)
    front_camera_flash = models.BooleanField()
    front_camera_video_features = models.TextField(blank=True)
    # Sound
    loudspeaker = models.CharField(max_length=100, choices=SPEAKER)
    audio_jack = models.CharField(max_length=100, choices=AUDIO_JACK)
    audio_features = models.CharField(max_length=200, blank=True)
    # Battery
    battery_capacity = models.CharField(max_length=200)
    battery_type = models.CharField(choices=BATTERY_TYPE, max_length=100)
    fast_charging = models.BooleanField(default=True)
    charging_output = models.CharField(max_length=200, blank=True)
    charging_port = models.CharField(max_length=100, choices=CHARGING_PORT)
    reverse_charging = models.BooleanField(default=True)
    wireless_charging = models.BooleanField()
    # Price
    starting_price = models.IntegerField()
    # Others
    fingerprint_sensor = models.CharField(choices=FINGERPRINT, max_length=200)
    face_unlock = models.BooleanField(default=True)
    other_sensors = models.TextField(blank=True)
    description = models.TextField(blank=True)
    rating = models.FloatField(blank=True)
    company_official_URL = models.URLField(null=True)

    def __str__(self):
        return str(self.phone_name)

    class Meta:
        verbose_name = 'Add New Phone'


class MobilePictures(models.Model):
    phone = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="phone_details_images/", default='static/img/default_photo_phone.jpg')

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Upload Phone Photo'


class Price(models.Model):
    phone = models.OneToOneField(Mobile, on_delete=models.CASCADE)
    amazon_price = models.FloatField(null=True, blank=True)
    flipkart_price = models.FloatField(null=True, blank=True)
    other_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Price on different site'


class LatestNews(models.Model):
    image = models.ImageField(upload_to='news_images/')
    title = models.CharField(max_length=200)
    highlights = models.TextField(blank=True)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def overview_lines(self):
        return filter(None, (line.strip() for line in self.highlights.splitlines()))

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Latest News'


class UpcomingPhones(models.Model):
    image = models.ImageField(upload_to='upcoming_smartphones_photos/', blank=True)
    name = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Upcoming Phones'
