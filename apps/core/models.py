from django.db import models

MAX_LENGHT = 100

class StemType(models.TextChoices):
    ERECT = 'Ereto', 'Caule Ereto'
    CLIMBING = 'Trepador', 'Caule Trepador'
    CRAWLING = 'Rastejante', 'Caule Rastejante'
    SCANDENT = 'Escandente', 'Caule Escandente'
    TUBER = 'Tubérculo', 'Caule Tubérculo'
    RHIZOME = 'Rizoma', 'Caule Rizoma'
    BULB = 'Bulbo', 'Caule Bulbo'
    RUNNER = 'Estolho', 'Caule Estolho'
    SARMENTOUS = 'Sarmentoso', 'Caule Sarmentoso'
    WOODY = 'Lenhoso', 'Caule Lenhoso'
    HERBACEOUS = 'Herbáceo', 'Caule Herbáceo'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class LeafType(models.TextChoices):
    SIMPLE = 'Simples', 'Folha Simples'
    COMPOUND = 'Composta', 'Folha Composta'
    PALMATE_COMPOUND = 'Palmaticomposta', 'Folha Palmaticomposta'
    PINNATE_COMPOUND = 'Pinnaticomposta', 'Folha Pinnaticomposta'
    BIPINNATE_COMPOUND = 'Bipinnaticomposta', 'Folha Bipinnaticomposta'
    TRIFOLIATE = 'Trifoliolada', 'Folha Trifoliolada'
    DIGITATE = 'Digitada', 'Folha Digitada'
    ACICULAR = 'Aciculada', 'Folha Aciculada'
    SCALE_LIKE = 'Escamosa', 'Folha Escamosa'
    SESSILE = 'Sésil', 'Folha Sésil'
    PETIOLED = 'Peciolada', 'Folha Peciolada'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class FlowerType(models.TextChoices):
    MALE = 'Masculino', 'Masculino'
    FEMALE = 'Feminino', 'Feminino'
    HERMAPHRODITE = 'Hemafrodita', 'Hermafrodita'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class FloweringPeriod(models.TextChoices):
    SPRING = 'Primavera', 'Primavera'
    SUMMER = 'Verão', 'Verão'
    AUTUMN = 'Outono', 'Outono'
    WINTER = 'Inverno', 'Inverno'
    ALL_YEAR = 'O ano todo', 'O ano todo'
    RAINY_SEASON = 'Estação chuvosa', 'Estação chuvosa'
    DRY_SEASON = 'Estação seca', 'Estação seca'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class FruitType(models.TextChoices):
    BERRY = 'Baga', 'Baga'
    DRUPE = 'Drupa', 'Drupa'
    LEGUME = 'Legume', 'Legume'
    SAMARA = 'Sâmara', 'Sâmara'
    CAPSULE = 'Cápsula', 'Cápsula'
    NUCUA = 'Núcua', 'Núcua'
    ACHENE = 'Aquênio', 'Aquênio'
    NUT = 'Noz', 'Noz'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class FruitingPeriod(models.TextChoices):
    SPRING = 'Primavera', 'Primavera'
    SUMMER = 'Verão', 'Verão'
    AUTUMN = 'Outono', 'Outono'
    WINTER = 'Inverno', 'Inverno'
    ALL_YEAR = 'O ano todo', 'O ano todo'
    RAINY_SEASON = 'Estação chuvosa', 'Estação chuvosa'
    DRY_SEASON = 'Estação seca', 'Estação seca'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class SoilType(models.TextChoices):
    SANDY = 'Arenoso', 'Solo Arenoso'
    CLAYEY = 'Argiloso', 'Solo Argiloso'
    SILTY = 'Siltoso', 'Solo Siltoso'
    LOAMY = 'Massapê', 'Solo Massapê'
    PEATY = 'Turfoso', 'Solo Turfoso'
    CHALKY = 'Calcário', 'Solo Calcário'
    SALINE = 'Salino', 'Solo Salino'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class MoistureLevel(models.TextChoices):
    LOW = 'Baixo', 'Baixo'
    MEDIUM = 'Médio', 'Médio'
    HIGH = 'Alto', 'Alto'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class LightExposure(models.TextChoices):
    FULL_SUN = 'Sol pleno', 'Sol pleno'
    PARTIAL_SHADE = 'Meia sombra', 'Meia sombra'
    SHADE = 'Sombra', 'Sombra'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class PredominantClimate(models.TextChoices):
    TROPICAL = 'Tropical', 'Tropical'
    SUBTROPICAL = 'Subtropical', 'Subtropical'
    TEMPERATE = 'Temperado', 'Temperado'
    ARID = 'Árido', 'Árido'
    MEDITERRANEAN = 'Mediterrâneo', 'Mediterrâneo'
    POLAR = 'Polar', 'Polar'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class WaterRequirement(models.TextChoices):
    LOW = 'Baixa', 'Baixa'
    MODERATE = 'Moderada', 'Moderada'
    HIGH = 'Alta', 'Alta'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class WateringFrequency(models.TextChoices):
    DAILY = 'Diária', 'Diária'
    TWICE_A_WEEK = 'Duas vezes por semana', 'Duas vezes por semana'
    WEEKLY = 'Semanal', 'Semanal'
    BIWEEKLY = 'Quinzenal', 'Quinzenal'
    MONTHLY = 'Mensal', 'Mensal'
    UNKNOWN = 'Desconhecido', 'Desconhecido'

class FertilizationType(models.TextChoices):
    ORGANIC = 'Orgânica', 'Orgânica'
    CHEMICAL = 'Química', 'Química'
    FOLIAR = 'Foliar', 'Foliar'
    NONE = 'Nenhuma', 'Nenhuma'

class BotanicalRegister(models.Model):
    # Botanical Identification
    binomial = models.CharField(max_length=250)
    common_name = models.CharField(max_length=250)
    botanical_family = models.CharField(max_length=250)
    genus = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    # Morphological
    height = models.FloatField()
    diameter = models.FloatField()
    stem_type = models.CharField(max_length=MAX_LENGHT, choices=StemType.choices, default=StemType.UNKNOWN)
    leaf_type = models.CharField(max_length=MAX_LENGHT, choices=LeafType.choices, default=LeafType.UNKNOWN)
    flower_type = models.CharField(max_length=MAX_LENGHT, choices=FlowerType.choices, default=FlowerType.UNKNOWN)
    flowering_period = models.CharField(max_length=MAX_LENGHT, choices=FloweringPeriod.choices, default=FloweringPeriod.UNKNOWN)
    fruit_type = models.CharField(max_length=MAX_LENGHT, choices=FruitType.choices, default=FruitType.UNKNOWN)
    fruiting_period = models.CharField(max_length=MAX_LENGHT, choices=FruitingPeriod.choices, default=FruitingPeriod.UNKNOWN)
    morphological_observations = models.TextField(blank=True, null=True)

    # Environmental Data
    soil_type = models.CharField(max_length=MAX_LENGHT, choices=SoilType.choices, default=SoilType.UNKNOWN)
    soil_pH = models.FloatField()
    moisture = models.CharField(max_length=MAX_LENGHT, choices=MoistureLevel.choices, default=MoistureLevel.UNKNOWN)
    lighting = models.CharField(max_length=MAX_LENGHT, choices=LightExposure.choices, default=LightExposure.UNKNOWN)
    temperature= models.FloatField()
    climate = models.CharField(max_length=MAX_LENGHT, choices=PredominantClimate.choices, default=PredominantClimate.UNKNOWN)

    # Cultivation
    water_requirement = models.CharField(max_length=MAX_LENGHT, choices=WaterRequirement.choices, default=WaterRequirement.UNKNOWN)
    watering_frequency = models.CharField(max_length=MAX_LENGHT, choices=WateringFrequency.choices, default=WateringFrequency.UNKNOWN)
    fertilization_type = models.CharField(max_length=MAX_LENGHT, choices=FertilizationType.choices, default=FertilizationType.NONE)
    need_for_pruning = models.BooleanField(default=False)
    susceptibility = models.TextField(blank=True, null=True)
    cultivation_notes = models.TextField(blank=True, null=True)

    # Location
    country = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    specific_location = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude_meters = models.FloatField(blank=True, null=True)
    biome = models.CharField(max_length=100, blank=True, null=True)
    ecosystem = models.CharField(max_length=150, blank=True, null=True)

    registration_date = models.DateField(auto_now_add=True)
    planting_date = models.DateField(blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)

    origin = models.CharField(max_length=100, blank=True, null=True)
    collection_number = models.CharField(max_length=100, blank=True, null=True)
    registered_by = models.CharField(max_length=150)

    general_image = models.ImageField(upload_to='plants/general/', null=True, blank=True)
    stem_image = models.ImageField(upload_to='plants/stem/', null=True, blank=True)
    leaf_image = models.ImageField(upload_to='plants/leaf/', null=True, blank=True)
    flower_image = models.ImageField(upload_to='plants/flower/', null=True, blank=True)
    fruit_image = models.ImageField(upload_to='plants/fruit/', null=True, blank=True)

    def __str__(self):
        return f'{self.binomial} ({self.common_name})'
