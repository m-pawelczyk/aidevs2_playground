Rozwiąż zadanie API o nazwie ‘md2html’. Twoim celem jest stworzenie za pomocą fine-tuningu modelu, który po otrzymaniu pliku Markdown na wejściu, zwróci jego sformatowaną w HTML wersję. Mamy tutaj jedno drobne utrudnienie, ponieważ znacznik pogrubienia jest konwertowany w bardzo nietypowy sposób.

Oto jak wygląda konwersja do HTML, którą chcemy otrzymać:

# Nagłówek1 = <h1>Nagłówek1</h1>
## Nagłówek2 = <h2>Nagłówek2</h2>
### Nagłówek3= <h3>Nagłówek3</h3>
**pogrubienie** = <span class="bold">pogrubienie</span>
*kursywa* = <em>kursywa</em>
[AI Devs 3.0](https://aidevs.pl) = <a href="https://aidevs.pl">AI Devs 3.0</a>
_podkreślenie_ = <u>podkreślenie</u>

Zaawansowana konwersja:
1. Element listy
2. Kolejny elementy

Wynik:
<ol>
<li>Element listy</li>
<li>Kolejny element</li>
</ol>

Tekst otrzymany z endpointa /task/ musisz przepuścić przez swój, wytrenowany model, a następnie zwrócić w standardowy sposób do /answer/.

Uwaga: do fine-tuningu użyj modelu gpt-3.5-turbo-0125. Istnieje ogromna szansa, że przy pierwszych podejściach do nauki modelu otrzymasz bardzo częste halucynacje. Zwiększ liczbę przykładów w pliku użytym do nauki i/lub pomyśl o zwiększeniu liczby cykli szkoleniowych. To zadanie da się rozwiązać bez fine tuningu, ale zależy nam, abyś jako kursant zaznajomił się z procesem uczenia modeli nowych umiejętności.

Dane wejściowe mogą zawierać zagnieżdżone znaczniki:

# Bardzo _ważny_ tekst = <h1> Bardzo <u>ważny</u> tekst</h1>

## HINT

1) Get task from /task/TOKEN

{
 "markdown":"## This is _important_ and **very cool**"
}

_____________________________________

2) Use your fine-tuned model to convert this input into HTML.
   Send it to /answer/TOKEN

{
 "answer":"<h2>This is <u>important</u> and <span class=\"bold\">very cool</span></h2>"
}

Rules:
1. Don't add any additional spaces and new lines
2. BOLD in this task is <span class="bold">any text</span>

_____________________________________

You don't know how to prepare JSONL file for fine-tuning?
This is "Zdzislaw mode". If you set "system" prompt to "tryb zdzislawa", all questions will be answered in Old Polish.