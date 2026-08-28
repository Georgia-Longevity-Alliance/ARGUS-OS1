# MHS (Model Hardware Standard) от Anthropic — анализ и применения для ARGUS

**Date:** 2026-08-28
**Status:** Analysis / opportunity mapping
**Author:** pi (for J. Tqemaladze)
**Relevance:** V9-BRAIN (Tool Bridge), DAIS (DAISocket), AIS LLM Bridge, V9-HANDS, OS1 Vision
**Sources:** anthropic.com (первоисточник, 27 авг 2026), modelhardwarestandard.com, explainx.ai, CNBC, arstechnica, techstartups, 3dnews (русскоязычный обзор)

---

## 1. Анализ новости (суть)

**27 авг 2026** Anthropic открыл **research preview** спецификации **Model Hardware Standard (MHS)** — общего стандарта, позволяющего ИИ-агентам безопасно управлять физическим лабораторным/производственным оборудованием. Родилось из коллаборации Anthropic (Alek Kemeny, Beneficial Deployments) и **HHMI Janelia Research Campus** (postdoc Arco Bast).

**Ключевые факты:**

- **Проблема:** интеграция оборудования в лаборатории занимает недели-месяцы; приборы не «разговаривают» друг с другом, нужны bespoke-интеграции специалистами.
- **Решение:** MHS — это **стандартизированный драйвер** поверх программируемого интерфейса любого прибора. Работает с любым устройством, у которого есть программируемый интерфейс. **Model-agnostic** (любой агент, не только Claude).
- **Абстракция — всего 2 примитива:** `read` (например «получить температуру») и `write` (например «установить температуру»). Плюс **discoverability** (стандартный формат обнаружения устройств в сети).
- **Физический/безопасностный контекст** (вес манипулятора, безопасные пределы лазера) записывается в **естественном языке** в «теги» драйвера — либо автором, либо путём **интервью агента с оператором**. Из тегов автоматически генерируется **reference file** (что устройство измеряет, что можно регулировать, какие safety-лимиты).
- **3 механизма управления:** ① MCP, ② CLI, ③ code files/APIs. Работают вместе: агент оркестрирует на высоком уровне, а для длинных/быстрых задач компилирует цепочки команд в **детерминированные скрипты**.
- **Главный паттерн:** «exploration → compile». Claude ведёт себя как учёный: настраивает лазер → смотрит через камеру результат → корректирует → когда понял последовательность, упаковывает в код-файл и дальше выполняет как одну команду.
- **Пилотные результаты:** Genentech (автономный BCA-анализ белка), UW Baker/Pinglay (удалённый мониторинг, qPCR, plate-handoff через LeRobot-руку), CMU (serial-dilution дозо-зависимые кривые ~×3 быстрее), **QuEra (стабилизация лазера на квантовом компьютере: 58% → 99.3%)**, Janelia (сжатие эксперимента с недель до дня).
- **Экосистема вендоров (10+):** AWS (Strands Robots), Automata (LINQ), Danaher, Doosan, MBF Bioscience (ScanImage), QIAGEN (QIAsphere Connect), Tecan (Fluent), Universal Robots, **Hugging Face (LeRobot)**, **Raspberry Pi (Camera MHS Driver)**.
- **Статус:** research preview по заявке (modelhardwarestandard.com); **open-source — позже**, после построения safety-roadmap (physical safety roadmap; обеспокоенность Anthopic про misuse — биооружие).

**Честные ограничения (важно для нас):**
- Физическое/пространственное рассуждение у LLM слабее человеческого. Пример Genentech: Claude воспринял ошибку из-за пузырьков в жидкости как «баг ПО», а не физическую проблему → нужен expert oversight и human-in-the-loop чекпоинты.
- Работает только с устройствами, у которых **есть** программируемый интерфейс.
- Safety-механизмы ещё в разработке.

---

## 2. Похожие новости / ландшафт (искал везде)

| # | Проект / стандарт | Что это | Связь с ARGUS |
|---|-------------------|---------|---------------|
| 1 | **Coscientist** (CMU, Nature 2023, s41586-023-06792-0) | GPT-4 автономно проектирует, планирует и выполняет хим. эксперименты; **Planner + Code Execution + Multi-Hardware** | V9-BRAIN уже взят как паттерн (раздел 4.3 V9_PROTOTYPE) |
| 2 | **OpentronsAI / Opentrons OT-2** | LLM генерирует протоколы для жидких манипуляторов по natural language; симуляция и верификация в чате; партнёрство с HighRes (agent-to-agent) | Если ARGUS добавляет liquid handler/автодозатор |
| 3 | **SiLA 2** (sila-standard.com) | Зрелый open стандарт аппаратной интероперабельности лабораторий (сообщения, данные), ориентирован на «Lab of the Future» | Может быть нашим transport-слоем помимо MCP |
| 4 | **Autoprotocol / ANLTRN** | JSON-язык описания экспериментов (Autoprotocol) и модель данных результатов (ANLTRN) — разделение дизайна и исполнения | Схема для переносимости протоколов OS1→OS2→OS3 |
| 5 | **LADS OPC UA** | Промышленный коммуникационный стандарт (корни в factory automation), защищённый | Альтернатива для индустриализации V9-HANDS |
| 6 | **FutureHouse (AI Scientist)** | Филантропический moonshot: полуавтономный ИИ-учёный (10 лет) | Родственный вектор — автономный цикл «design-build-test-learn» |
| 7 | **MCP (Model Context Protocol)** | Уже используется в ARGUS как «MCP-like» Tool Bridge | Прямой мост: MHS — это «MCP для физического железа» |
| 8 | **Anthropic Claude Science** (3dnews 1144365) | ИИ-модель для помощи учёным в болезнях/лекарствах | Контекст рынка |
| 9 | **OpenAI Codex + манипулятор** (UFactory xArm, «рисует цветок») | Пример LLM→робот-рука | Подтверждение паттерна exploration→compile |
| 10 | **AI-driven QC для liquid handling** (Springer 10489-025-06334-3) | CV-контроль качества жидких манипуляторов (Opentrons OT-2) | Vision как источник ground-truth — ровно наш YOLO+CellPose |

**Вывод из ландшафта:** ARGUS уже сидит на «переднем крае» этого тренда: у нас есть Tool Bridge (MCP-like), Safety Layer (Body Law), локальный LLM-мозг, Flight Recorder, Vision. MHS — это **экосистемный стандарт**, с которым ARGUS стоит выравниться, чтобы не изобретать свой driver-слой заново и получить совместимость с экосистемой (LeRobot, Tecan, OpenFlexure, Raspberry Pi).

---

## 3. Прямая карта: MHS ↔ ARGUS (V9 / DAIS)

| Компонент ARGUS | Соответствие в MHS | Действие |
|-----------------|--------------------|----------|
| **Tool Bridge** (V9 4.3, «MCP-like») | MHS driver (read/write + discoverability) | Кандидат реализовать Tool Bridge **по спецификации MHS** ⇒ совместимость с агентами/вендорами |
| **Safety Layer / Body Law** (force ≤5 N, speed ≤200 mm/s, no-touch zones) | natural-language safety tags + reference file | Перенести наши safety-лимиты в MHS-теги драйвера (интервью-паттерн) |
| **Flight Recorder** (AIS: pose, force, time, frame) | «streams state back to agent» | Оставить свой Event Store; MHS читает его как источник состояния |
| **V9-BRAIN** (Planner + LLM) | MCP/CLI/code orchestration от агента | Наш локальный мозг = «harness», MHS = транспорт |
| **Vision (YOLO+CellPose на AGX)** | camera driver / ground-truth | Камера — и датчик, и ground-truth для верификации действий |
| **V9-HANDS (кабельные руки)** | robotic arm driver (write: move/gripper; read: pose/force) | Написать MHS-драйвер «arm» поверх нашего контроллера |
| **Pipette/дозатор** | liquid handler driver | Если добавим автодозатор — собственный драйвер |
| **FOSH манипулятор** | robotic/positioning driver | read/write позиции |

**Стратегическая позиция:** MHS ещё **не open-source** (только заявка). Для ARGUS это:
1. **Подать заявку** на research preview (modelhardwarestandard.com) — показать автономную микроскопию live-cell как use-case.
2. **Пока ждём open-source** — смоделировать свой Tool Bridge по «форме» MHS (read/write примитивы + discoverable + natural-language safety tags), чтобы после релиза просто заменить transport.
3. ARGUS-OS1 как **первый инстанс AIS/DAIS** — это отличный «полигон» для MHS: открытая, дешёвая, с живым use-case.

---

## 4. Референс-код для ARGUS (решения под MHS-стиль)

### 4.1 Минимальный MHS-стиль драйвер-абстракция (Python, edge)

Универсальная обёртка «read/write + safety», чтобы любой прибор (микроскоп, рука, насос, FOSH) экспонировать как MHS-совместимое устройство. Работает на Jetson Orin NX / AGX.

```python
# argus_mhs/driver.py — MHS-style driver base for ARGUS devices
from __future__ import annotations
import json, time, threading
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

@dataclass
class Tag:
    """Natural-language safety/physical context (MHS 'tags').
    Заменяет paper manuals: вес, лимиты, что можно мерить/регулировать.
    Именно это MHS генерирует в reference file."""
    description: str            # e.g. "Cable-driven arm, 6 DOF, through glove port"
    weight_kg: float            # важна для безопасного манипулирования
    read: List[str]             # measurable quantities
    write: List[str]            # adjustable quantities
    safety_limits: Dict[str, Any]  # enforced by Safety Layer / Body Law
    units: Dict[str, str] = field(default_factory=dict)

class MHSDriver:
    """Base class. Two primitives: read / write + discoverability."""
    def __init__(self, device_id: str, tag: Tag, logger=None):
        self.id = device_id
        self.tag = tag
        self._state: Dict[str, Any] = {}
        self._lock = threading.Lock()
        self.flight = []                 # Flight Recorder (AIS)
        self._log = logger or print

    # ---- primitives ----
    def read(self, qty: str) -> Any:
        """read(qty) -> value. Domain-validated against tag.read."""
        if qty not in self.tag.read:
            raise KeyError(f"{self.id}: '{qty}' not readable (allowed={self.tag.read})")
        with self._lock:
            val = self._read_impl(qty)
        self._record("read", qty, val)
        return val

    def write(self, qty: str, value: Any) -> Any:
        """write(qty, value). Safety-checked via Body Law before execute."""
        if qty not in self.tag.write:
            raise KeyError(f"{self.id}: '{qty}' not writable")
        self._enforce_safety(qty, value)                  # Safety Layer
        self._checkpoint(qty, value)                      # human-in-the-loop hook
        with self._lock:
            out = self._write_impl(qty, value)
        self._record("write", qty, {"cmd": value, "res": out})
        return out

    # ---- subclasses override these ----
    def _read_impl(self, qty):   raise NotImplementedError
    def _write_impl(self, qty, value): return None

    def _enforce_safety(self, qty, value):
        lim = self.tag.safety_limits.get(qty)
        if lim:
            mn, mx = lim.get("min"), lim.get("max")
            if (mn is not None and value < mn) or (mx is not None and value > mx):
                raise PermissionError(f"{self.id}: {qty}={value} violates {lim}")

    def _checkpoint(self, qty, value):
        """Human-in-the-loop gate for irreversible ops (MHS lesson: Genentech bubbles)."""
        if self.tag.safety_limits.get(qty, {}).get("confirm"):
            ok = input(f"CONFIRM {self.id}: {qty}={value}? [y/N] ")
            if ok.strip().lower() not in ("y", "yes"):
                raise RuntimeError(f"aborted by operator: {qty}={value}")

    def _record(self, kind, qty, payload):
        self.flight.append({"t": time.time(), "dev": self.id,
                            "kind": kind, "qty": qty, "payload": payload})
        self._log(f"[{self.id}] {kind} {qty} -> {payload}")

    # ---- discoverability (MHS standard format) ----
    def discover(self) -> dict:
        return {
            "id": self.id, **self.tag.__dict__,
            "online": True,
            "transport": ["mcp", "cli", "code"],
        }

    def reference_file(self) -> str:
        """Auto-generated reference (what MHS builds from tags)."""
        return json.dumps(self.discover(), indent=2, default=str)
```

### 4.2 Драйвер «рука» (V9-HANDS) — позиция + gripper, с Body Law

```python
# argus_mhs/arm.py — cable-driven V9 arm driver
from argus_mhs.driver import MHSDriver, Tag

ARM_TAG = Tag(
    description="Cable-driven 6-DOF arm through glove port sleeve",
    weight_kg=2.5,                        # нужно для безопасного подъёма
    read=["pose", "force", "speed", "current", "gripper"],
    write=["move", "gripper", "speed_limit", "force_limit"],
    safety_limits={
        "force":     {"max": 5.0},        # Body Law: F<=5 N
        "speed":     {"max": 200.0},      # Body Law: v<=200 mm/s
        "move":      {"min": [-200,-200,-200], "max": [200,200,200], "confirm": True},
    },
    units={"pose": "mm", "force": "N", "speed": "mm/s"},
)

class ArmDriver(MHSDriver):
    def __init__(self, bus, arm="L", node_id=0x11):
        super().__init__(f"argus/arm/{arm}", ARM_TAG)
        self.bus = bus; self.node_id = node_id
        self._pose = [0, 0, 0]            # start at home

    def _read_impl(self, qty):
        if qty == "pose":  return self._pose
        if qty == "force": return self.bus.read_reg(self.node_id, 0x30) / 1000.0
        if qty == "speed": return self.bus.read_reg(self.node_id, 0x32)
        return 0

    def _write_impl(self, qty, value):
        if qty == "gripper":
            self.bus.write_reg(self.node_id, 0x40, 1 if value else 0)
            return "ok"
        if qty == "move":
            # простая интерполяция, скорость под Body Law
            self._move_to(value)
            return self._pose
        return None

    def _move_to(self, target):
        n = int(self.tag.safety_limits["speed"]["max"]**0.5)  # шагов по скорости
        cur = list(self._pose)
        for k in range(1, n + 1):
            step = [cur[i] + (target[i]-cur[i])*k/n for i in range(3)]
            for i in range(3):  # жёсткий лимит скорости за шаг
                d = abs(step[i]-cur[i])
                if d / 0.05 > self.tag.safety_limits["speed"]["max"]:
                    step[i] = cur[i] + (1 if step[i] > cur[i] else -1) * \
                              self.tag.safety_limits["speed"]["max"] * 0.05
            self.bus.move_to(self.node_id, step)
            self._pose = step
            time.sleep(0.05)  # tick
```

### 4.3 Драйвер «микроскоп» (OpenFlexure) — пример интеграции с Motor Release API

```python
# argus_mhs/microscope.py — OpenFlexure stage + focus
from argus_mhs.driver import MHSDriver, Tag
import math

SCOPE_TAG = Tag(
    description="OpenFlexure microscope (ARGUS-OS1), 40x/0.75 dry",
    weight_kg=4.0,
    read=["stage_xyz", "focus", "temperature", "snr"],
    write=["move_stage", "set_focus", "capture", "led"],
    safety_limits={
        "move_stage": {"min": [0,0,0], "max": [30,30,15]},   # ход стола
        "set_focus":  {"min": 0, "max": 20},
        "led":        {"min": 0, "max": 100, "confirm": False},
    },
    units={"stage_xyz": "mm", "focus": "mm", "temperature": "C"},
)

class ScopeDriver(MHSDriver):
    def __init__(self, hw):   # hw = OpenFlexure control / Motor Release API
        super().__init__("argus/scope", SCOPE_TAG)
        self.hw = hw

    def _read_impl(self, qty):
        if qty == "stage_xyz": return self.hw.position()
        if qty == "focus":     return self.hw.focus_position()
        if qty == "temperature": return self.hw.temp()
        if qty == "snr":       return self.hw.report_snr()   # из Vision
        return None

    def _write_impl(self, qty, value):
        if qty == "move_stage":  self.hw.move_abs(value); return self.hw.position()
        if qty == "set_focus":   self.hw.focus_abs(value); return self.hw.focus_position()
        if qty == "capture":     return self.hw.capture(value)   # path/name
        if qty == "led":         self.hw.set_led(value); return "ok"
```

### 4.4 Паттерн «exploration → compile» (MHS) для ARGUS

Тот самый приём: пока агент не понимает процесс — рассуждает по шагам с камерой (Vision); как понял — компилирует детерминированный скрипт.

```python
# argus_mhs/explore_compile.py — learn a procedure, then run it deterministically
import json

def explore_and_compile(driver, goal, callback, max_steps=20):
    """Итеративно настраивает прибор, смотрит результат, записывает цепочку."""
    chain = []
    for step in range(max_steps):
        action = callback.pick_next_action(step, chain)   # агент решает -> write()
        result = driver.write(action["qty"], action["value"])
        obs = callback.observe(result)                    # camera/Vision snapshot
        chain.append({"qty": action["qty"], "value": action["value"], "obs": obs})
        if callback.is_done(obs):
            return compile_script(chain)                  # -> deterministic code
    raise TimeoutError("not converged")

def compile_script(chain):
    """Упаковываем цепочку в детерминированный код-файл (single command)."""
    lines = ["def run(driver):"]
    for i, c in enumerate(chain):
        lines.append(f"    r{i} = driver.write({c['qty']!r}, {c['value']!r})")
    lines.append("    return locals()")
    src = "\n".join(lines)
    with open("compiled_procedure.py", "w") as f:
        f.write(src)
    return src
```

**Пример применения из V9:** автофокус / настройка объектива 60x/1.2 WI по SNR — агент двигает focus, читает SNR от Vision, повторяет; сходится → компилирует скрипт `focus_60x.py`, дальше выполняется как одна команда (то же, что QuEra сделал с лазером).

### 4.5 MCP-сервер поверх драйверов (transport, model-agnostic)

MHS использует MCP как один из транспортов. Лёгкий MCP-сервер, экспонирующий наши драйверы:

```python
# argus_mhs/mcp_server.py — expose ARGUS drivers over MCP
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ARGUS")

_devices = {}   # id -> MHSDriver

def register(driver): _devices[driver.id] = driver

@mcp.tool()
def list_devices() -> str:
    return json.dumps([d.discover() for d in _devices.values()], indent=2)

@mcp.tool()
def read(device: str, qty: str) -> str:
    return json.dumps(_devices[device].read(qty))

@mcp.tool()
def write(device: str, qty: str, value) -> str:
    return json.dumps(_devices[device].write(qty, value))

if __name__ == "__main__":
    register(ArmDriver(...)); register(ScopeDriver(...))
    mcp.run()   # stdio transport; подключается к любому MCP-aware агенту
```

### 4.6 Natural-language «теги» через интервью (паттерн MHS)

MHS позволяет заполнять контекст драйвера через **интервью агента с оператором**. Это ценно для ARGUS: оператор (не инженер) описывает прибор словами, агент превращает в теги.

```python
# argus_mhs/interview.py — build a Tag by interviewing the operator
QUESTIONS = [
    ("как называется прибор / что измеряет?", "description"),
    ("какой вес устройства (кг)?", "weight_kg"),
    ("что он МОЖЕТ измерять?", "read"),
    ("что можно РЕГУЛИРОВАТЬ?", "write"),
    ("какие безопасные пределы (мин/макс)?", "safety_limits"),
    ("в каких единицах?", "units"),
]
def interview(fn=input) -> Tag:
    d = {}
    for q, key in QUESTIONS:
        raw = fn(q).strip()
        d[key] = json.loads(raw) if key in ("read","write","safety_limits","units") else raw
    return Tag(**d)
```

---

## 5. Рекомендуемые действия для ARGUS (action items)

1. **[Приоритет] Подать заявку на research preview MHS** (modelhardwarestandard.com) — use-case: автономная live-cell микроскопия, слёжка родословной клеток, V9-HANDS 24/7. Для ERC/grant материалов — это валидация подхода «LLM управляет железом».
2. **Выровнять Tool Bridge с формой MHS** — даже до open-source смоделировать свой драйвер-слой (read/write + discover + NL-safety-tags), чтобы после релиза просто сменить transport (свой → MHS). Сэкономит переделку.
3. **Перенести Safety Layer/Body Law в MHS-теги** — наш `force<=5N, speed<=200mm/s, no-touch zones` уже есть; переложить как safety_limits в референс-драйверы.
4. **Внедрить human-in-the-loop чекпоинты** на необратимые операции (урок Genentech: LLM путает физическую ошибку с багом ПО). Наш `_checkpoint` / escalation rule `confidence<0.7 → человек`.
5. **Следить за экосистемой**: Hugging Face интегрирует MHS в **LeRobot** (открытая рука), Raspberry Pi Camera driver, Tecan Fluent. ARGUS-OS3 уже на открытых руках — совместимость с LeRobot усилит FOSH/V9-HANDS.
6. **Добавить liquid-handler-driver** к портфелю OS2 (V7 микрофлюидика) — автодозатор с read/write (Opentrons/Tecan урок) + CV-QC (Vision).
7. **Документировать**: записать паттерн «exploration→compile» в CONCEPT/METHODOLOGY — сильный аргумент для грантов (EIC Pathfinder 28 окт — WP2 argus).

---

## 6. Источники и ссылки

- Первоисточник: https://www.anthropic.com/news/model-hardware-standard-research-preview (27 авг 2026)
- Подача заявки: https://www.modelhardwarestandard.com/
- Разбор (MCP-аналогия, вендоры, лимиты): https://explainx.ai/blog/anthropic-model-hardware-standard-mhs-research-preview-august-2026
- LANDSCAPE: Coscientist Nature 2023 https://www.nature.com/articles/s41586-023-06792-0
- OpentronsAI https://opentrons.com/ai ; SiLA 2 https://sila-standard.com ; Autoprotocol vs SiLA2 (inferensys)
- FutureHouse https://www.futurehouse.org/
- 3dnews (русский обзор): https://3dnews.ru/1147628/...
- Смежное в ARGUS: `docs/V9_PROTOTYPE.md`, `docs/STERILIZATION_TRANSFER.md`, `../DAIS/README.md`

---

*ENG/научное — можно пушить в GLA ARGUS-OS1. Bез писем/ревью. MHS ещё не OS — не публиковать как «мы интегрированы» до релиза, только как «мы следуем паттерну».*
