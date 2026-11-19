# ARGUS-OS1 — приёмка скана: что запустить у микроскопа

Пакет самодостаточный: питон-скрипты + официальная прошивка `nano.hex` (Sangaboard v1.0.4) +
runbook. Ничего скачивать не нужно.

## 0. Что нужно от вас

Микроскоп включён и доступен по сети; у вас есть доступ к его серверу (обычно
`http://microscope.local:5000` или `http://<IP>:5000`).

## 1. Установить зависимости (один раз)

```bash
python3 -m pip install --user numpy opencv-python scipy scikit-image
```

## 2. Прогнать приёмку

```bash
cd pipeline
./v6_accept.sh --discover                        # найти сервер сам
# либо явно:
./v6_accept.sh --url http://microscope.local:5000 --scan <папка_скана>
```

Без скана (только проверка «сервер ↔ прошивка»):

```bash
./v6_accept.sh --url http://microscope.local:5000
```

С измерением хода стадии (если есть кадры медленного прохода по одной оси):

```bash
./v6_accept.sh --url http://microscope.local:5000 --scan <папка> \
               --rom-frames <папка_траверса> --step-um <командный шаг в мкм>
```

## 3. Что получится

* `hardware/acceptance_<дата>.md` — таблица A1–A7 с вердиктом (`PASS` / `FAIL` / `UNKNOWN`);
* `stitched_<дата>.tif` — сшитая мозаика (если указан `--scan`);
* exit-код 0 только если все проверки PASS.

`UNKNOWN` — это не ошибка, а «не удалось проверить»: молчание не считается согласием.

## 4. Что прислать обратно

```bash
tar -czf argus_acceptance_$(date +%F).tar.gz hardware/acceptance_*.md stitched_*.tif
```

## 5. Проверить сам пакет, не трогая микроскоп

```bash
cd pipeline && ./v6_accept.sh --demo      # полная цепочка на синтетическом фантоме
python3 -m pytest ../tests/test_pipeline.py -q
```

## Что означают проверки

| # | Проверка | Провал означает |
|---|---|---|
| A1 | сервер не ругается на прошивку | прошить `firmware/vendor/sangaboard-v1.0.4/nano.hex` (AVRDUDESS: preset `Arduino Nano (ATMega328P)` → Program); см. runbook §1 |
| A2 | `motor_release` доступен по API | нужен для ухода от перегрева в CO₂-инкубаторе |
| A3/A4 | скан согласован с `scan_data.json` | классика: тайлы 1400 px вместо 2800 (`histo scan capture mode = full`, патч `things/autofocus.py`) |
| A5 | измеренный ход стадии в норме | повторить траверс с перекрытием ≥30 %, больше текстуры в поле |
| A6 | ≤100 нм/px, бининг ≤2×2 | сменить объектив/бининг: выше ~150 нм/px пары центриолей сливаются |
| A7 | швы < 1.05 | уменьшить overlap-шаг (0.35–0.50 на неровных образцах) или проверить фокус-стек |
