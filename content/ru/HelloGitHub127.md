# 《HelloGitHub》Выпуск 127
> Интерес — лучший учитель, а **HelloGitHub** помогает заинтересоваться открытым кодом!

> **Перевод на русский:** Александр Давыдов (Aleksandr Davydenko), [@kotuke](https://github.com/kotuke) · Оригинал: [HelloGitHub №127](https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub127.md) · Лицензия: CC BY-NC-ND 4.0 · Перевод также опубликован на [kotuke.ru](https://kotuke.ru/521xueweihan/127.html)
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Содержание

Нажмите значок **«Содержание»** в правом верхнем углу, чтобы открыть оглавление — так читать удобнее.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Совет**: если картинки не загружаются, [нажмите сюда](https://hellogithub.com/periodical/volume/127) и откройте выпуск другим способом.

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
Подписывайтесь на официальный аккаунт «HelloGitHub» в WeChat, чтобы получать выпуски первыми
</p>

## Содержание выпуска
> **Материалы этого выпуска**｜Обновляется **28-го** числа каждого месяца

### Проекты на C
1、[cbirds](https://hellogithub.com/periodical/statistics/click?target=https://github.com/clainstone/cbirds)：Стая птиц в терминале. Утилита на C имитирует полёт по алгоритму Boids и рисует стаю брайлевской точечной матрицей. Есть трёхмерный режим, охота орла, часы, которые стая складывает буквами, и режим экранной заставки.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1067126172.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[colibri](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JustVugg/colibri)：Модели на 100&nbsp;млрд параметров без видеокарты. Движок инференса моделей со смесью экспертов (MoE) написан на чистом C: ни зависимостей, ни GPU. В памяти остаётся только та часть модели, которая нужна всегда, а веса остальных экспертов читаются с диска, когда до них доходит очередь. От 8&nbsp;ГБ памяти уже можно запускать открытые модели GLM, Kimi, DeepSeek, Qwen и другие; есть API, совместимые с OpenAI и Anthropic. Работает на Windows, Linux и macOS.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1286080397.png' style="max-width:80%; max-height=80%;"></img></p>

3、[DEsk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fyzugx/DEsk)：Рабочий стол Linux в виде письменного стола. Окружение на Wayland, где вся комната рисуется трассировкой лучей. Стол деревянный, окна — листы бумаги: при сворачивании складываются, как письмо, а при закрытии сминаются в комок и выбрасываются.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1413289247.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на C#
4、[Filee](https://hellogithub.com/periodical/statistics/click?target=https://github.com/KnifeLemon/Filee)：Конвертация формата перетаскиванием. Офлайн-конвертер на C# понимает больше 200 форматов: изображения, PDF, документы Office, электронные книги, аудио и видео, архивы, CAD и другие. Удерживая Ctrl, перетащите файл — рядом с курсором появится кольцо форматов; отпустите на нужном, и преобразование готово. Файлы никуда не загружаются. Работает на Windows, Linux и macOS. Поделился [@Adnan Bhaldar](https://hellogithub.com/user/jAlIvVMhn0kcEsU)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1396526702.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на C++
5、[EditHere](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Inginnng/EditHere)：Правки интерфейса для ИИ со скриншота. Инструмент аннотаций для ИИ-программирования собирает, что именно менять, в JSON, который модель читает напрямую. Умеет узнавать элементы интерфейса при наведении, ставить точки и рамки, двигать компоненты, чтобы поправить раскладку, ставить видео на паузу и помечать кадр за кадром, а также распознавать текст и делать длинные снимки. Вся обработка идёт на машине пользователя.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1365889199.gif' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на Go
6、[gocryptfs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rfjakob/gocryptfs)：Шифрованная файловая система на Go. Инструмент на Go и FUSE монтирует каталог с шифротекстом как обычный каталог для чтения и записи: содержимое файлов и их имена шифруются по отдельности. Готовый каталог можно положить в Dropbox и другие облака или синхронизировать инкрементально через rsync.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/41997606.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[magpie](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yetone/magpie)：Смена модели у ИИ-помощника в один клик. Менеджер на Go подключает Kimi к Claude Code, а DeepSeek — к Codex. Локальный шлюз переводит форматы API OpenAI, Anthropic и Gemini и работает с разными помощниками и поставщиками моделей. Подпиской можно поделиться с другими помощниками, а когда лимит кончается, аккаунт переключается сам.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1383809012.png' style="max-width:80%; max-height=80%;"></img></p>

8、[matcha](https://hellogithub.com/periodical/statistics/click?target=https://github.com/floatpane/matcha)：Почта в терминале. Клиент на Go и Bubble Tea принимает и отправляет письма командами. Несколько учётных записей, письма в Markdown и маркетплейс плагинов. Поделился [@Drew Smirnoff](https://hellogithub.com/user/FYa6zrBtyeSOsLu)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1027531184.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[pocket-id](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pocket-id/pocket-id)：Свой сервер входа без пароля. Сервис идентификации OIDC и OAuth 2.0 на Go заменяет пароль на Passkey. Пароль помнить не нужно: для входа достаточно аппаратного ключа вроде YubiKey.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/841141075.png' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на JavaScript
10、[GeoLibre](https://hellogithub.com/periodical/statistics/click?target=https://github.com/opengeos/GeoLibre)：Открытая ГИС в браузере. Геоинформационная система на TypeScript визуализирует геоданные, даёт их просматривать и анализировать, и сами данные остаются на машине. Больше 1000 инструментов анализа работают в браузере через WebAssembly: рельеф, гидрология, лидар и дистанционное зондирование. Запускается в браузере, на компьютере, на телефоне и в Jupyter Notebook; есть подложки Луны, Марса и других планет.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1251648409.png' style="max-width:80%; max-height=80%;"></img></p>

11、[omni-tools](https://hellogithub.com/periodical/statistics/click?target=https://github.com/iib0011/omni-tools)：Набор онлайн-инструментов на своём сервере. Коллекция на React закрывает повседневные задачи: картинки, аудио и видео, PDF, текст, дата и время, математика и обработка данных. Все файлы обрабатываются локально в браузере. Есть масштаб и смена формата изображений, обрезка видео, разбиение и склейка PDF, перевод часовых поясов, работа с JSON и другое.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/814882742.png' style="max-width:80%; max-height=80%;"></img></p>

12、[openGym](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DuarteSantos8/openGym)：Дневник тренировок, где данные остаются у вас. Учёт тренировок и веса без подписки, рекламы и телеметрии разворачивается у себя одной командой Docker. Больше 5000 упражнений с анимированными демонстрациями, планы по дням недели, тренировка с подсказками, таймер отдыха между подходами, автоматические личные рекорды и тепловая карта мышц. Данные импортируются из Strong, Hevy и других приложений. Есть версии для iPhone, Apple Watch и Android.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1305213943.png' style="max-width:80%; max-height=80%;"></img></p>

13、[puter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HeyPuter/puter)：Облачный компьютер в браузере. Настольная операционная система в браузере собирает файлы, приложения и игры в одном месте и открывается откуда угодно. Встроены блокнот, диктофон, таблицы, камера и другие программы. Разработчикам доступны ИИ, облачное хранилище, база «ключ — значение» и Serverless Workers, а свои веб-приложения и игры можно выкладывать в магазин.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/766341786.png' style="max-width:80%; max-height=80%;"></img></p>

14、[word-atlas](https://hellogithub.com/periodical/statistics/click?target=https://github.com/designfuchen/word-atlas)：Слова IELTS: одно слово — одна картинка. Бесплатное открытое веб-приложение для заучивания лексики IELTS работает в браузере и не просит регистрации. Больше 7000 ключевых слов: у каждого своя иллюстрация, два авторских примера и британское и американское произношение. Повторения расписывает алгоритм FSRS, а выученное слово зажигает звезду на трёхмерной карте лексики.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1432980411.png' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на Kotlin
15、[aerial-tv](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pengchujin/aerial-tv)：Рабочий стол телевизора в духе Apple TV. Открытый лаунчер Android TV по образцу tvOS: без рекламы и ленты рекомендаций, сам запускается при включении. Подходит для китайских телевизоров Xiaomi, TCL, Skyworth и других, а также для приставок и проекторов. Умеет раскладывать приложения, заводить папки, прятать системные программы и сортировать их с телефона по QR-коду. Root не нужен, вернуть прежний лаунчер можно в любой момент.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1426780056.jpg' style="max-width:80%; max-height=80%;"></img></p>

16、[DiPlay](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shihabal3amri/DiPlay)：CarPlay на головном устройстве Android. Приложение для автомобильной магнитолы на Android даёт проводной и беспроводной CarPlay. Есть прямое подключение по Wi-Fi и автомобильная точка доступа; стрелку поворота, расстояние и название улицы можно вывести на проекционный дисплей. Настраиваются размер значков, разрешение и частота кадров. Нужен Android 7.0 и новее, интерфейс есть и на упрощённом китайском.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1385817306.png' style="max-width:80%; max-height=80%;"></img></p>

17、[DroidDeck](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Droid-Deck/DroidDeck)：Игры Steam на Android. Приложение переносит SteamOS на Android и запускает клиент Steam на устройствах с графическим процессором Adreno. Можно играть в игры для Windows, ставить программы Linux и входить в магазины GOG, Epic и Amazon.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1385776214.gif' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на Python
18、[genanki](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kerrickstaley/genanki)：Колоды Anki из Python. Библиотека собирает колоды карточек: свои поля заметок, шаблоны карточек и стили CSS, картинки и аудио. После правки колоду генерируют заново и импортируют ещё раз — карточки с тем же именем заменяются. Удобно делать карточки пачками из списков слов, банков вопросов и других данных.

19、[kcc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ciromattia/kcc)：Комиксы для экранов на электронных чернилах. Конвертер подгоняет комиксы под Kindle, Kobo и другие читалки: картинки, CBZ, PDF и прочие файлы становятся электронной книгой, страницы масштабируются под разрешение устройства, поля обрезаются.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/6938242.png' style="max-width:80%; max-height=80%;"></img></p>

20、[manimgx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/academa-labs/manimgx)：Более быстрый движок математической анимации. Трёхмерный движок с API, совместимым с редакцией Manim Community, рисует на GPU и работает в 90 раз быстрее версии сообщества. Анимацию можно писать прямо из Claude Code, Codex и других ИИ-помощников, запускать в браузере через WebGPU или сохранять в MP4.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1406372374.png' style="max-width:80%; max-height=80%;"></img></p>

21、[pywinauto](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pywinauto/pywinauto)：Автоматизация программ Windows из Python. Библиотека имитирует мышь и клавиатуру в окнах, диалогах и элементах управления и умеет читать текст с интерфейса. Два бэкенда — Win32 API и MS UI Automation; элементы ищутся по заголовку окна, имени контрола и другим текстовым свойствам. Нескольких строк хватает, чтобы открыть меню, нажать кнопку и ввести текст. Подходит для автотестов настольных программ и повторяющихся действий.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/36223210.png' style="max-width:80%; max-height=80%;"></img></p>

22、[tilelang](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tile-ai/tilelang)：Быстрые ядра для GPU на Python. Предметный язык для операторов под GPU, CPU и NPU построен на компиляторе TVM: GEMM, FlashAttention и другие ядра можно довести до предела без ручного низкоуровневого кода. Поддерживаются NVIDIA CUDA, AMD ROCm, Apple Metal и Huawei Ascend (китайские ИИ-ускорители). Есть автоподбор параметров, наглядная отладка и примеры операторов больших моделей, в том числе DeepSeek MLA.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/867004514.png' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на Rust
23、[esp32sim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mikroverk/esp32sim)：Открытый симулятор ESP32. Симулятор на Rust запускает нетронутую прошивку на компьютере или в браузере — плата не нужна. Полностью воспроизводит загрузку от бутлоадера до FreeRTOS и умеет имитировать экран, касания, светодиоды, звук, камеру, Wi-Fi и другую периферию. Поддерживаются чипы ESP32-S3, C3, C6, P4 и другие.

24、[miniserve](https://hellogithub.com/periodical/statistics/click?target=https://github.com/svenstaro/miniserve)：Минимальный HTTP-сервер для раздачи файлов. Утилита командной строки на Rust — один файл, которым по HTTP открывают доступ к файлам и каталогам. Есть вход по имени и паролю, загрузка файлов, скачивание папки архивом, поиск по имени, вход по QR-коду, TLS и WebDAV. README.md рисуется как на GitHub, темы — светлая и тёмная. Удобно, когда файлы нужно отдать ненадолго. Поделился [@size_t](https://hellogithub.com/user/6xC1sQERhkZVB7A)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/131135585.png' style="max-width:80%; max-height=80%;"></img></p>

25、[OpenShell](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NVIDIA/OpenShell)：Песочница NVIDIA для ИИ-агентов. Среда выполнения для автономных агентов: агент читает и пишет файлы, ставит пакеты и вызывает API, но не получает произвольный доступ к данным, ключам и сети. Каждый агент работает в изолированной песочнице, а политика на уровне ядра ограничивает файлы, системные вызовы и сетевые соединения. Настоящие учётные данные подставляются только тогда, когда запрос уходит на уже одобренный адрес.

### Skills
26、[anatomy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wheresryan22/anatomy)：Технические идеи как движущиеся механизмы. Навык иллюстраций для ИИ-помощников превращает отвлечённые понятия в настоящие подвижные механизмы и рисует их аккуратной интерактивной изометрией. Попадание в кеш, например, становится личинкой замка, которая проворачивается, только если все штифты встали на место. Три вида: SVG, SVG с шейдерами WebGL и 3D. На выходе — страница HTML, файл SVG или компонент React. Поделился [@JRZYgit](https://hellogithub.com/user/0Aj4ipeQrDYuHBX)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1410124849.png' style="max-width:80%; max-height=80%;"></img></p>

27、[asd-ste100-skill](https://hellogithub.com/periodical/statistics/click?target=https://github.com/danyuchn/asd-ste100-skill)：Инструкции для ИИ на упрощённом английском. Навык опирается на норму упрощённого технического английского аэрокосмической отрасли и переписывает расплывчатые, многословные фразы так, чтобы их нельзя было прочитать двояко, а затем отдаёт текст ИИ-агенту. Каждое предложение проверяется на страдательный залог, сложные времена, несколько команд сразу, длину и рекламные прилагательные. При правке не теряется ни один факт и ни одно условие оригинала.

28、[diagram-design](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cathrynlavery/diagram-design)：Диаграммы с чувством дизайна от ИИ. Навык для ИИ-помощников собирает файлы HTML+SVG, которые открываются прямо в браузере. 45 типов: схемы архитектуры, блок-схемы, диаграммы последовательности, Ганта, Санки и другие. Умеет снимать фирменные цвета и шрифты с сайта, перерисовывать готовые схемы из Mermaid, draw.io и Excalidraw в одном стиле и сохранять результат в PNG или SVG.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1212769188.png' style="max-width:80%; max-height=80%;"></img></p>

29、[impeccable](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pbakaus/impeccable)：Больше вкуса в интерфейсах, которые собирает ИИ. Навык фронтенд-дизайна для ИИ-помощников расширяет официальный frontend-design от Anthropic и уводит генерацию от однотипных экранов: шрифт Inter на всём, фиолетово-синий градиент, карточки внутри карточек. 24 команды оформления — polish, audit, critique и другие — и 62 детерминированных правил проверки. Подходит для Claude Code, Cursor, Codex, Gemini CLI и других инструментов.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1097346685.png' style="max-width:80%; max-height=80%;"></img></p>

### Проекты на Swift
30、[tendedero](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alejandrobujan/tendedero)：Скриншоты сушатся на верёвке у верхнего края экрана. Небольшая утилита для macOS вешает каждый снимок на верёвку вверху, как бельё. Курсор к строке меню — верёвка опускается, курсор ушёл — сама убирается, и стол не завален файлами скриншотов. Щелчок копирует, долгое нажатие открывает пометки, перетаскивание в программу сразу отправляет снимок, перетаскивание в корзину удаляет. Есть и нарезка записи экрана.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1408099862.gif' style="max-width:80%; max-height=80%;"></img></p>

31、[xtool](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xtool-org/xtool)：Кроссплатформенная замена Xcode. Инструмент на Swift собирает приложения iOS через SwiftPM и ставит их на настоящее устройство — на Linux, Windows и macOS. Создание проекта, сборка и запуск, подпись и установка, управление устройствами, а из командной строки — ещё и сервисы Apple Developer.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/889784913.png' style="max-width:80%; max-height=80%;"></img></p>

### Искусственный интеллект
32、[artemis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google/artemis)：Телефон под управлением ИИ от Google. Средство автоматизации Android: задачу описывают обычным языком, и модель сама управляет телефоном или эмулятором — тестовые сценарии через несколько приложений и повседневные дела. Встроенный сервер MCP даёт Claude Code, Codex и другим помощникам напрямую управлять телефоном и забирать логи со скриншотами. Подходят мультимодальные модели Gemini, Claude, GPT-4o и другие.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1333399642.png' style="max-width:80%; max-height=80%;"></img></p>

33、[DeepInfer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/deepseek-ai/DeepInfer)：Фреймворк инференса от DeepSeek. На этом высокопроизводительном фреймворке DeepSeek держит свой крупный онлайн-сервис: здесь ядро и для офлайн-инференса, и для развёртывания в большом масштабе. Встроены собственные оптимизированные ядра FlashMLA, DeepGEMM, DeepEP и другие. Есть параллелизм данных для внимания, параллелизм экспертов MoE, асинхронное планирование, детерминированная выборка и структурированный вывод. Работает на NVIDIA и на NPU Huawei Ascend.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1421825221.png' style="max-width:80%; max-height=80%;"></img></p>

34、[harness2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google-research/harness2)：Агент, который улучшает сам себя, от Google. Фреймворк позволяет ИИ-агенту становиться лучше на незнакомой задаче, не трогая веса модели. Под текущую задачу он предлагает правки — системный промпт, память, навыки, субагенты и плагины — и прогоняет варианты, сравнивая, что вышло, а затем сохраняет опыт для следующих задач.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1407951147.png' style="max-width:80%; max-height=80%;"></img></p>

35、[UniMate](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Friedrich-M/UniMate)：Любой 3D-персонаж двигается по одной фразе. Генерация движений для моделей с разным скелетом: на вход — модель со скелетом и текстовое описание, на выходе — движение в реальном времени. Переучивать модель под каждый скелет не нужно. Подходят люди, четвероногие, птицы, морские существа, насекомые, механизмы и другие конструкции.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1309249926.png' style="max-width:80%; max-height=80%;"></img></p>

36、[VoiceStudio](https://hellogithub.com/periodical/statistics/click?target=https://github.com/debpalash/VoiceStudio)：Локальная студия ИИ-голоса. Клонирование голоса и озвучка целиком на своей машине, открытая замена ElevenLabs; больше 600 языков. Внутри CosyVoice, IndexTTS, GPT-SoVITS, WhisperX и другие движки синтеза и распознавания. Проектирование тембра, озвучка видео, отделение голоса, расшифровка речи и аудиокниги.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1206390571.gif' style="max-width:80%; max-height=80%;"></img></p>

### Прочее
37、[everything](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HeyPuter/everything)：Открытые замены коммерческих программ с нуля. Проект команды Puter заново собирает бесплатные открытые аналоги коммерческого ПО. Уже больше 50 приложений: замены Excel, PowerPoint, Photoshop, AutoCAD, Zoom и Slack, плюс небольшие игры — шахматы, судоку и другие. Большинство открывается прямо в браузере.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1417456983.png' style="max-width:80%; max-height=80%;"></img></p>

38、[Future-Style-Periodic-Table](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SeanWong17/Future-Style-Periodic-Table)：Таблица Менделеева в стиле киберпанк. Интерактивная таблица в браузере, тёмная: все 118 элементов, атомный номер, электронная конфигурация, изотопы, валентность и другие данные. Тепловые карты переключаются по атомному радиусу, электроотрицательности, температуре плавления и другим свойствам. Щелчок по элементу — и трёхмерную модель атома можно крутить, разглядывая электронные оболочки. Интерфейс на китайском и английском.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1107726420.png' style="max-width:80%; max-height=80%;"></img></p>

39、[gpu-unlock](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Zagitta/gpu-unlock)：Разблокировка вычислений у видеокарт RTX 30. Модуль ядра Linux поднимает темп выдачи инструкций FP16/BF16 у потребительских карт NVIDIA RTX 30-й серии до уровня соответствующей профессиональной карты, и пропускная способность матричных операций заметно растёт. У RTX 3090 Ti, например, производительность BF16 вырастает с 87,5 до 157,4&nbsp;TFLOPS, а предзаполнение больших моделей ускоряется на 14–36&nbsp;%. Разблокировка выполняется до загрузки официального драйвера NVIDIA: сам драйвер менять не нужно, и после каждого обновления заново его патчить тоже не приходится.

40、[navigation2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ros-navigation/navigation2)：Навигация для мобильных роботов. Фреймворк автономной навигации даёт восприятие, локализацию, планирование пути, управление движением и объезд препятствий; модули собираются в сценарий деревом поведения. Кроме обычного маршрута есть обход путевых точек, следование за целью и навигация с полным покрытием.

41、[PicLite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/amiaoapp/PicLite)：Локальное сжатие картинок без лишнего. Обработка изображений и анимаций на своей машине: пакетное сжатие, сравнение качества перетаскиванием, смена формата, масштаб и водяные знаки. Программа сама сравнивает варианты JPEG, WebP, PNG и другие и оставляет файл меньшего размера. Есть приложения для Windows, macOS и Linux, а также браузер и Docker; картинки не уходят с компьютера. В настольной версии — слежение за папкой, автоматическая оптимизация буфера обмена и подключение по MCP.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1314868034.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Открытые книги
42、[HowToLiveBetter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eternity4719/HowToLiveBetter)：«Руководство по выгодной жизни» (《高性价比人生指南》). Книга на китайском о том, как меньшими деньгами, временем и силами получить больше лет жизни и денег. Долголетие и профилактика болезней, первая помощь, экономия и личные финансы, границы закона, помощь безработным, китайское медицинское страхование и социальное обеспечение, отношения, брак и дети, легальное оформление своего дела.



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub126.md">«Предыдущий выпуск»</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Отзывы и предложения</a> | «Следующий выпуск»
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>Расскажите о своём проекте с открытым кодом!</a> 👈<br>
    В WeChat найдите <strong>HelloGitHub</strong> и подпишитесь на аккаунт<br>
    — так вы получите выпуски первыми и сможете участвовать в акциях для подписчиков<br>
    Если картинки в тексте не загружаются, нажмите <a href='https://hellogithub.com/periodical/volume/127'>здесь</a>.
</p>

## Заявление
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="Лицензия Creative Commons" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>Оригинал распространяется по лицензии <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">«Атрибуция — Некоммерческое использование — Без производных 4.0 Всемирная»</a> (CC BY-NC-ND 4.0).

Перевод выполнил Александр Давыдов (Aleksandr Davydenko), https://github.com/kotuke — некоммерческая публикация с указанием авторства оригинала. Оригинал: <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub127.md">HelloGitHub №127</a>.
