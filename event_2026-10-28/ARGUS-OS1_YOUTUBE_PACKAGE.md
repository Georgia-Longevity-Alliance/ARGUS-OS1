# ARGUS-OS1 — YouTube Publication Package (2026-10-28)

Полный пакет для публикации трёх версий лекции. Видео и транскрипты — на Desktop.

## 📹 Видео (готовы, на Desktop)
| Версия | Файл | Длительность | Канал |
|---|---|---|---|
| EN | `ARGUS-OS1_2026-10-28_LECTURE.mp4` | 26.7 мин | youtube.com/@DrJabaTqemaladze |
| RU | `ARGUS-OS1_2026-10-28_LECTURE_RU.mp4` | 28.9 мин | youtube.com/@DrJabaTqemaladze |
| KA | `ARGUS-OS1_2026-10-28_LECTURE_KA.mp4` | 33.4 мин | youtube.com/@ჯაბაექიმი |

## 📝 Транскрипты (для комментариев)
`ARGUS-OS1_TRANSCRIPT_EN.txt` · `ARGUS-OS1_TRANSCRIPT_RU.txt` · `ARGUS-OS1_TRANSCRIPT_KA.txt`
(закрепить полный текст как pinned comment)

---

## EN — youtube.com/@DrJabaTqemaladze

**Title:**
ARGUS-OS1: An Open-Source AI-First Microscope for Longevity Science

**Description:**
ARGUS-OS1 is an open-source, AI-first microscope for longevity science. A ~$3K instrument that sees, tracks, and decides entirely on hardware you own, with no cloud dependency. Built on the OpenFlexure frame with a Jetson edge processor, it closes the acquire → segment → track → schedule loop on-device, and adds a verifiable AI layer (DAIS) with provenance on every claim.

In this lecture: why C. elegans, the centriole pedigree hypothesis, the open build (optics + edge AI + local compute), the phototoxicity and closed-box differentiator, and the roadmap OS1 → OS2 → OS3 → OS4.

- Repo: github.com/Georgia-Longevity-Alliance/ARGUS-OS1
- Jaba Tqemaladze, MD — Georgia Longevity Alliance · jaba@longevity.ge

Full transcript in the pinned comment. Open build, open data, open questions.

**Pinned comment:**
[full text from ARGUS-OS1_TRANSCRIPT_EN.txt]

---

## RU — youtube.com/@DrJabaTqemaladze

**Title:**
ARGUS-OS1: открытый микроскоп с ИИ для науки о долголетии

**Description:**
ARGUS-OS1 — открытый микроскоп с искусственным интеллектом для науки о долголетии. Прибор примерно за $3K, который видит, прослеживает и решает целиком на вашем оборудовании, без облака. На базе рамы OpenFlexure и краевого процессора Jetson он замыкает контур «съёмка → сегментация → отслеживание → планирование» на устройстве и добавляет проверяемый слой ИИ (DAIS) с происхождением у каждого утверждения.

В этой лекции: почему C. elegans, гипотеза о родословной центриолей, открытая сборка (оптика + ИИ на краю + локальные вычисления), отличительная черта — фототоксичность и закрытый обслуживаемый бокс, и дорожная карта OS1 → OS2 → OS3 → OS4.

- Репозиторий: github.com/Georgia-Longevity-Alliance/ARGUS-OS1
- Джаба Ткемаладзе, MD — Грузинская ассоциация долголетия · jaba@longevity.ge

Полный текст — в закреплённом комментарии.

**Закреплённый комментарий:**
[полный текст из ARGUS-OS1_TRANSCRIPT_RU.txt]

---

## KA — youtube.com/@ჯაბაექიმი

**Title:**
ARGUS-OS1: ღია მიკროსკოპი ხელოვნური ინტელექტით ხანგრძლივობის მეცნიერებისთვის

**Description:**
ARGUS-OS1 — ღია მიკროსკოპი ხელოვნური ინტელექტით ხანგრძლივობის მეცნიერებისთვის. დაახლოებით $3K-იანი ინსტრუმენტი, რომელიც ხედავს, აკვირდება და წყვეტს მთლიანად თქვენს ტექნიკაზე, ღრუბლის გარეშე. OpenFlexure-ის ჩარჩოზე და Jetson-ის კიდის პროცესორზე დაფუძნებული, ის ხურავს კონტურს „გადაღება → სეგმენტაცია → თვალთვალი → დაგეგმვა“ მოწყობილობაზე და ამატებს გადამოწმებადი ხელოვნური ინტელექტის ფენას (DAIS) ყოველი მტკიცების წარმომავლობით.

ამ ლექციაში: რატომ C. elegans, ცენტრიოლის გენეალოგიის ჰიპოთეზა, ღია აწყობა (ოპტიკა + ხელოვნური ინტელექტი კიდეზე + ლოკალური გამოთვლები), გამორჩეული თვისება — ფოტოტოქსიკურობა და დახურული მომსახურებადი ყუთი, და საგზაო რუკა OS1 → OS2 → OS3 → OS4.

- რეპოზიტორია: github.com/Georgia-Longevity-Alliance/ARGUS-OS1
- ჯაბა თქემალაძე, MD — საქართველოს ხანგრძლივობის ალიანსი · jaba@longevity.ge

სრული ტექსტი — დაფიქსირებულ კომენტარში.

**დაფიქსირებული კომენტარი:**
[სრული ტექსტი ARGUS-OS1_TRANSCRIPT_KA.txt-დან]

---

## ⚙️ Как загрузить (нужно от тебя)

Загрузка на YouTube требует авторизации твоего аккаунта. Я не могу выполнить её за тебя — нужны твои credentials. Подготовлено:

1. **Скрипт загрузки** — `~/Desktop/Services/scripts/yt_upload_argus.py` (Python + google-api-python-client).
2. **Что нужно сделать один раз:**
   - В Google Cloud Console создать OAuth 2.0 Client ID (Desktop app), скачать `client_secret.json`
   - Поставить: `pip install google-api-python-client google-auth-oauthlib`
   - Запустить: `python3 yt_upload_argus.py en` (первый запуск откроет браузер → войти в нужный аккаунт → разрешить)
   - То же для `ru` (на @DrJabaTqemaladze) и `ka` (на @ჯაბაექიმი — войти в этот аккаунт)
3. **Заголовки, описания и тексты комментариев** — в этом файле выше; скрипт возьмёт их из `ARGUS-OS1_YOUTUBE_PACKAGE.md` по языку.

**Альтернатива (быстрее):** если у тебя уже есть доступ к Google/YouTube API и токен — дай путь к `client_secret.json`, и я запущу загрузку.

---

*Джаба Ткемаладзе, Грузинская ассоциация долголетия · 2026-10-28*
