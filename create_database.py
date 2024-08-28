from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask uygulamasını başlatın
app = Flask(__name__)

# Veritabanı URI'sini ayarlayın (SQLite kullanıyoruz)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy ORM'i başlatın
db = SQLAlchemy(app)

# Veritabanı için Soru Modelini Tanımlayın
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)
    option4 = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(100), nullable=False)

# Veritabanını oluşturun
with app.app_context():
    db.create_all()

# Örnek soruları veritabanına ekleyin
def add_sample_questions():
    q1 = Question(
        text="Yapay zeka (AI) nedir?",
        option1="A. Bir bilgisayar oyunu",
        option2="B. Bilgisayarların insan gibi düşünmesini sağlama",
        option3="C. Bir matematik dersi",
        option4="D. Bir film",
        correct_option="option2"
    )
    q2 = Question(
        text="Yapay zeka ile bilgisayara ne öğretmeye çalışıyoruz?",
        option1="A. Eğlenceli oyunlar oynamayı",
        option2="B. Bilgiyi analiz etmeyi ve karar vermeyi",
        option3="C. Resim çizmeyi",
        option4="D. Müzik dinlemeyi",
        correct_option="option2"
    )
    q3 = Question(
        text="Yapay zeka sistemlerinde verileri analiz etmek için kullanılan terim nedir?",
        option1="A. Programlama",
        option2="B. Veri analizi",
        option3="C. Oyun geliştirme",
        option4="D. Web tasarımı",
        correct_option="option2"
    )

    q4 = Question(
        text="Bir yapay zeka modelinin iyi sonuçlar vermesi için ne tür veriler kullanmalıyız?",
        option1="A. Çok eski ve güncel olmayan veriler",
        option2="B. Kafamız karışmasın diye rastgele veriler",
        option3="C. Doğru ve güncel veriler",
        option4="D. Herhangi bir veri",
        correct_option="option3"
    )

    q5 = Question(
        text="Yapay zeka modelini değerlendirmek için kullanılan terim nedir?",
        option1="A. Eğitim",
        option2="B. Test",
        option3="C. Oyun",
        option4="D. Geri bildirim",
        correct_option="option2"
    )

    q6 = Question(
        text="Bir yapay zeka modelinin doğru tahminler yapması için ne gerekir?",
        option1="A. Eğitilmiş ve test edilmiş olması",
        option2="B. Yalnızca eğitilmiş olması",
        option3="C. Yalnızca test edilmiş olması",
        option4="D. Hiçbir şey gerekmez",
        correct_option="option1"
    )
    q7 = Question(
        text="Yapay zeka nasıl öğrenir?",
        option1="A. Her gün bilgisayarın içinde gezerek",
        option2="B. Verilerden ve örneklerden öğrenerek",
        option3="C. İnternetteki videoları izleyerek",
        option4="D. Kitapları okuyarak",
        correct_option="option2"
    )
    q8 = Question(
        text="Yapay zeka projelerinde bir modelin performansını ölçmek için hangi araçlar kullanılır?",
        option1="A. Eğitim kitapları",
        option2="B. Grafikler ve metrikler",
        option3="C. Oyun seviyeleri",
        option4="D. Resimler",
        correct_option="option2"
    )
    q9 = Question(
        text="Yapay zeka modelinde bir 'sinir ağı' nedir?",
        option1="A. Bilgisayarın gücünü artıran bir araç",
        option2="B. İnsan beynine benzer bir yapı",
        option3="C. Renkli grafikler çizen bir program",
        option4="D. Oyun karakterlerini hareket ettiren bir yazılım",
        correct_option="option2"
    )
    q10 = Question(
        text="Bir yapay zeka modelinin doğru tahminler yapması için ne gereklidir?",
        option1="A. Yeterli veri ve doğru eğitim",
        option2="B. Hızlı bir internet bağlantısı",
        option3="C. Güçlü bir bilgisayar ekranı",
        option4="D. Yüksek sesli hoparlörler",
        correct_option="option1"
    )

    with app.app_context():
        db.session.add_all([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10])
        db.session.commit()

add_sample_questions()