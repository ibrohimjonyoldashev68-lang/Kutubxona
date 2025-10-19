from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Author, Genre, Book, Member, Kirim, Chiqim, Xabar


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate(self, attrs):
        nomi = attrs.get("nomi")
        if not nomi or len(nomi.strip()) == 0:
            raise ValidationError({"nomi": "Muallif nomi bo‘sh bo‘lishi mumkin emas."})
        return attrs

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    def validate(self, attrs):
        nomi = attrs.get("nomi")
        if not nomi or len(nomi.strip()) == 0:
            raise ValidationError({"nomi": "Janr nomi bo‘sh bo‘lishi mumkin emas."})
        return attrs

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        miqdori = attrs.get("miqdori", 0)
        mavjud = attrs.get("mavjud", 0)
        if miqdori < 0:
            raise ValidationError({"miqdori": "Kitob soni manfiy bo‘lishi mumkin emas."})
        if mavjud < 0:
            raise ValidationError({"mavjud": "Mavjud kitob soni manfiy bo‘lishi mumkin emas."})
        if mavjud > miqdori:
            raise ValidationError({"mavjud": "Mavjud soni umumiy sonidan ko‘p bo‘lishi mumkin emas."})
        return attrs

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    def validate(self, attrs):
        fio = attrs.get("fio")
        if not fio or len(fio.strip()) == 0:
            raise ValidationError({"fio": "F.I.O bo‘sh bo‘lishi mumkin emas."})
        return attrs

    def create(self, validated_data):
        return Member.objects.create(**validated_data)


class KirimSerializer(ModelSerializer):
    class Meta:
        model = Kirim
        fields = '__all__'

    def validate(self, attrs):
        miqdori = attrs.get("miqdori", 1)
        if miqdori <= 0:
            raise ValidationError({"miqdori": "Kirim miqdori 0 yoki manfiy bo‘lishi mumkin emas."})
        return attrs

    def create(self, validated_data):
        book = validated_data['book']
        miqdor = validated_data.get('miqdori', 1)
        book.mavjud += miqdor
        book.umumiy_soni += miqdor
        book.save()
        return Kirim.objects.create(**validated_data)


class ChiqimSerializer(ModelSerializer):
    class Meta:
        model = Chiqim
        fields = '__all__'

    def validate(self, attrs):
        book = attrs.get("book")
        miqdori = attrs.get("miqdori", 1)

        if miqdori <= 0:
            raise ValidationError({"miqdori": "Chiqim miqdori 0 yoki manfiy bo‘lishi mumkin emas."})

        if book and book.mavjud < miqdori:
            raise ValidationError({"miqdori": f"Faqat {book.mavjud} ta kitob mavjud."})

        return attrs

    def create(self, validated_data):
        book = validated_data['book']
        miqdor = validated_data.get('miqdori', 1)
        book.mavjud -= miqdor
        book.sarflangan_soni += miqdor
        book.save()
        return Chiqim.objects.create(**validated_data)



class XabarSerializer(ModelSerializer):
    class Meta:
        model = Xabar
        fields = '__all__'