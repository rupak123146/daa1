from flask import Flask, render_template, request
import time

app = Flask(__name__)

def brute_force_intersection(a, b):
    result = []
    for i in a:
        if i in b and i not in result:
            result.append(i)
    return result

def presorting_intersection(a, b):
    a.sort()
    b.sort()
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    method = None
    time_taken = None
    time_complexity = ""
    space_complexity = ""

    if request.method == 'POST':
        list_a = request.form['list_a']
        list_b = request.form['list_b']
        method = request.form['method']

        a = list(map(int, list_a.split()))
        b = list(map(int, list_b.split()))

        start_time = time.time()
        if method == 'brute':
            result = brute_force_intersection(a, b)
            time_complexity = "O(n × m)"
            space_complexity = "O(min(n, m))"
        elif method == 'presort':
            result = presorting_intersection(a, b)
            time_complexity = "O(n log n + m log m)"
            space_complexity = "O(min(n, m))"
        end_time = time.time()

        time_taken = round(end_time - start_time, 6)

    return render_template(
        'index.html',
        result=result,
        method=method,
        time_taken=time_taken,
        time_complexity=time_complexity,
        space_complexity=space_complexity
    )

if __name__ == '__main__':
    app.run(debug=True)
