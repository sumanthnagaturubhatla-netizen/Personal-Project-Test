from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import smtplib
from email.mime.text import MIMEText

# ---------------- FLASK APP ----------------

app = Flask(__name__)

CORS(app)

# ---------------- DATABASE CONNECTION ----------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="online_exam",
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

# ---------------- HOME ROUTE ----------------

@app.route('/')
def home():

    return "Online Mock Test Backend Running Successfully"

# ---------------- REGISTER API ----------------

@app.route('/register', methods=['POST'])
def register():

    try:

        data = request.json

        fullname = data['fullname']
        email = data['email']

        sql = """
        INSERT INTO users(fullname,email)
        VALUES(%s,%s)
        """

        values = (fullname, email)

        cursor.execute(sql, values)

        db.commit()

        return jsonify({

            "success": True,
            "message": "Registration Successful"

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        })

# ---------------- FINAL TEST PART 1 ----------------

@app.route('/submit_test1', methods=['POST'])
def submit_test1():

    try:

        data = request.json

        sql = """
        INSERT INTO final_test1
        (user_email,q1,q2,q3,q4,q5,q6,q7,q8)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (

            data['email'],
            data['q1'],
            data['q2'],
            data['q3'],
            data['q4'],
            data['q5'],
            data['q6'],
            data['q7'],
            data['q8']
        )

        cursor.execute(sql, values)

        db.commit()

        return jsonify({

            "success": True,
            "message": "Final Test Part-1 Submitted Successfully"

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        })

# ---------------- FINAL TEST PART 2 ----------------

@app.route('/submit_test2', methods=['POST'])
def submit_test2():

    try:

        data = request.json

        sql = """
        INSERT INTO final_test2
        (user_email,q1,q2,q3,q4,q5,q6,q7,q8)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (

            data['email'],
            data['q1'],
            data['q2'],
            data['q3'],
            data['q4'],
            data['q5'],
            data['q6'],
            data['q7'],
            data['q8']
        )

        cursor.execute(sql, values)

        db.commit()

        # ---------------- CORRECT ANSWERS TEST 1 ----------------

        answers1 = [

            "25%",
            "64",
            "$2,240",
            "90",
            "His son",
            "Quiet",
            "West",
            "10"
        ]

        # ---------------- CORRECT ANSWERS TEST 2 ----------------

        answers2 = [

            "Frank",
            "Extravagant",
            "Thorough",
            "Unlikely",
            "LIFO",
            "Both A and B are true",
            "5",
            "Syntax = grammar mistake, Runtime = during execution"
        ]

        # ---------------- FETCH TEST 1 ----------------

        cursor.execute("""

        SELECT q1,q2,q3,q4,q5,q6,q7,q8
        FROM final_test1
        WHERE user_email=%s
        ORDER BY id DESC
        LIMIT 1

        """, (data['email'],))

        test1 = cursor.fetchone()

        # ---------------- FETCH TEST 2 ----------------

        cursor.execute("""

        SELECT q1,q2,q3,q4,q5,q6,q7,q8
        FROM final_test2
        WHERE user_email=%s
        ORDER BY id DESC
        LIMIT 1

        """, (data['email'],))

        test2 = cursor.fetchone()

        score1 = 0
        score2 = 0

        # ---------------- CALCULATE TEST 1 SCORE ----------------

        if test1:

            for i in range(8):

                if str(test1[i]).strip() == answers1[i]:

                    score1 += 1

        # ---------------- CALCULATE TEST 2 SCORE ----------------

        if test2:

            for i in range(8):

                if str(test2[i]).strip() == answers2[i]:

                    score2 += 1

        total_score = score1 + score2

        # ---------------- PASS OR FAIL ----------------

        if total_score >= 8:

            status = "PASS"

        else:

            status = "FAIL"

        # ---------------- EMAIL CONFIGURATION ----------------

        sender_email = "sumanthnagaturubhatla@gmail.com"

        sender_password = "vllz urkb eudc odgo"

        # ---------------- EMAIL MESSAGE ----------------

        message = f"""

Hello Student,

Your Online Mock Test Result form Nag's Academy

--------------------------------

Final Test Part-1 Score : {score1}/8

Final Test Part-2 Score : {score2}/8

Total Score : {total_score}/16

Status : {status}

--------------------------------

Thank You

Nag's Academy
"""

        msg = MIMEText(message)

        msg['Subject'] = "Online Mock Test Result FROM NAG'S ACADEMY"

        msg['From'] = sender_email

        msg['To'] = data['email']

        # ---------------- SEND EMAIL ----------------

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender_email, sender_password)

        server.send_message(msg)

        server.quit()

        return jsonify({

            "success": True,
            "message": "Final Test Part-2 Submitted Successfully",
            "test1_score": score1,
            "test2_score": score2,
            "total_score": total_score,
            "status": status

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        })

# ---------------- RUN SERVER ----------------

if __name__ == '__main__':

    app.run(debug=True)
