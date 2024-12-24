from app import db, app  # Import `app` to push the application context
from models import Quiz, Content

def seed_quiz_questions():
    with app.app_context():  # Push the app context
        questions = [
            Quiz(
                question="What is the capital of France?",
                option_a="Berlin",
                option_b="Madrid",
                option_c="Paris",
                option_d="Rome",
                correct_option="C"
            ),
            Quiz(
                question="Which programming language is used for web development?",
                option_a="Python",
                option_b="HTML",
                option_c="Java",
                option_d="C++",
                correct_option="B"
            ),
            Quiz(
                question="What is 5 + 3?",
                option_a="7",
                option_b="8",
                option_c="9",
                option_d="10",
                correct_option="B"
            ),
            Quiz(
                question="Which data structure uses FIFO (First In, First Out)?",
                option_a="Stack",
                option_b="Queue",
                option_c="Array",
                option_d="Tree",
                correct_option="B"
            ),
            Quiz(
                question="What is the result of 3 * 4?",
                option_a="7",
                option_b="10",
                option_c="12",
                option_d="14",
                correct_option="C"
            ),
            Quiz(
                question="Which programming language is known as 'object-oriented'?",
                option_a="HTML",
                option_b="CSS",
                option_c="Java",
                option_d="SQL",
                correct_option="C"
            ),
            Quiz(
                question="What does HTTP stand for?",
                option_a="HyperText Transfer Protocol",
                option_b="HyperText Transformation Protocol",
                option_c="HyperTransfer Text Protocol",
                option_d="None of the above",
                correct_option="A"
            ),
            Quiz(
                question="What is the binary representation of the decimal number 5?",
                option_a="101",
                option_b="110",
                option_c="111",
                option_d="100",
                correct_option="A"
            ),
            Quiz(
                question="What is the time complexity of binary search?",
                option_a="O(n)",
                option_b="O(log n)",
                option_c="O(n^2)",
                option_d="O(1)",
                correct_option="B"
            ),
            Quiz(
                question="Which of the following is a NoSQL database?",
                option_a="MySQL",
                option_b="PostgreSQL",
                option_c="MongoDB",
                option_d="SQLite",
                correct_option="C"
            ),
        ]

        # Add to the database
        db.session.bulk_save_objects(questions)
        db.session.commit()
        print("Quiz questions seeded successfully!")

def seed_content():
    with app.app_context():
        content_items = [
            # Beginner Content
            Content(
                title="Introduction to Python Programming",
                topic="Programming Basics",
                difficulty="Beginner",
                description="Learn the basics of Python programming, including syntax, variables, and simple programs.",
                content_url="https://www.youtube.com/watch?v=rfscVS0vtbw"
            ),
            Content(
                title="HTML Basics for Web Development",
                topic="Web Development",
                difficulty="Beginner",
                description="Learn the fundamentals of HTML, including tags, attributes, and creating simple web pages.",
                content_url="https://www.youtube.com/watch?v=UB1O30fR-EE"
            ),
            Content(
                title="Understanding SQL and Databases",
                topic="Databases",
                difficulty="Beginner",
                description="Learn how to use SQL for managing and querying relational databases.",
                content_url="https://www.youtube.com/watch?v=HXV3zeQKqGY"
            ),
            Content(
                title="Introduction to Data Structures",
                topic="Programming Basics",
                difficulty="Beginner",
                description="Learn the basic concepts of data structures such as arrays, lists, and stacks.",
                content_url="https://www.youtube.com/watch?v=bum_19loj9A"
            ),
            Content(
                title="Beginner's Guide to Algorithms",
                topic="Algorithms",
                difficulty="Beginner",
                description="Understand the basics of algorithms and their importance in programming.",
                content_url="https://www.youtube.com/watch?v=rL8X2mlNHPM"
            ),
            Content(
                title="Basics of Bootstrap for Web Design",
                topic="Web Development",
                difficulty="Beginner",
                description="Learn how to use Bootstrap to build responsive web pages.",
                content_url="https://www.youtube.com/watch?v=5GcQtLDGXy8"
            ),

            # Intermediate Content
            Content(
                title="Object-Oriented Programming in Python",
                topic="Intermediate Topics",
                difficulty="Intermediate",
                description="Dive into the concepts of object-oriented programming using Python, including classes, objects, and inheritance.",
                content_url="https://www.youtube.com/watch?v=Ej_02ICOIgs"
            ),
            Content(
                title="Building Responsive Websites with Bootstrap",
                topic="Web Development",
                difficulty="Intermediate",
                description="Learn how to use Bootstrap to create responsive and visually appealing websites.",
                content_url="https://www.youtube.com/watch?v=QAgrHLtG1Yk"
            ),
            Content(
                title="Database Design and Normalization",
                topic="Intermediate Databases",
                difficulty="Intermediate",
                description="Understand database design concepts and normalization techniques.",
                content_url="https://www.youtube.com/watch?v=-iwCmKnvf5E"
            ),
            Content(
                title="Algorithms and Time Complexity",
                topic="Algorithms",
                difficulty="Intermediate",
                description="Understand algorithms and analyze their time complexity for better performance.",
                content_url="https://www.youtube.com/watch?v=9TlHvipP5yA"
            ),
            Content(
                title="Python Libraries for Data Analysis",
                topic="Data Analysis",
                difficulty="Intermediate",
                description="Explore Python libraries like Pandas and NumPy for data analysis.",
                content_url="https://www.youtube.com/watch?v=vmEHCJofslg"
            ),
            Content(
                title="JavaScript ES6 Features",
                topic="Web Development",
                difficulty="Intermediate",
                description="Master JavaScript ES6 features like arrow functions, promises, and modules.",
                content_url="https://www.youtube.com/watch?v=NCwa_xi0Uuc"
            ),

            # Advanced Content
            Content(
                title="Advanced Data Structures in Python",
                topic="Programming",
                difficulty="Advanced",
                description="Explore advanced data structures like heaps, trees, and graphs to enhance your problem-solving skills.",
                content_url="https://www.youtube.com/watch?v=8hly31xKli0"
            ),
            Content(
                title="Scaling Databases with NoSQL",
                topic="Advanced Databases",
                difficulty="Advanced",
                description="Explore the principles and use cases of NoSQL databases for handling large-scale data.",
                content_url="https://www.youtube.com/watch?v=qI_g07C_Q5I"
            ),
            Content(
                title="Dynamic Programming: Concepts and Examples",
                topic="Algorithms",
                difficulty="Advanced",
                description="Learn dynamic programming techniques for solving complex problems.",
                content_url="https://www.youtube.com/watch?v=oBt53YbR9Kk"
            ),
            Content(
                title="Deep Dive into REST APIs",
                topic="Web Development",
                difficulty="Advanced",
                description="Understand the principles of REST API design and implementation.",
                content_url="https://www.youtube.com/watch?v=Q-BpqyOT3a8"
            ),
            Content(
                title="Machine Learning Basics with Python",
                topic="Machine Learning",
                difficulty="Advanced",
                description="Learn the basics of machine learning using Python libraries like Scikit-Learn.",
                content_url="https://www.youtube.com/watch?v=7eh4d6sabA0"
            ),
            Content(
                title="React.js for Advanced Web Applications",
                topic="Web Development",
                difficulty="Advanced",
                description="Master React.js to build advanced, interactive web applications.",
                content_url="https://www.youtube.com/watch?v=w7ejDZ8SWv8"
            ),
            Content(
                title="Understanding GraphQL APIs",
                topic="Web Development",
                difficulty="Advanced",
                description="Learn how GraphQL APIs differ from REST and how to implement them in projects.",
                content_url="https://www.youtube.com/watch?v=ed8SzALpx1Q"
            ),
            Content(
                title="Kubernetes for Application Deployment",
                topic="DevOps",
                difficulty="Advanced",
                description="Learn how to use Kubernetes to deploy, scale, and manage containerized applications.",
                content_url="https://www.youtube.com/watch?v=X48VuDVv0do"
            )
        ]

        # Add to the database
        db.session.bulk_save_objects(content_items)
        db.session.commit()
        print("20 Content items seeded successfully!")

if __name__ == "__main__":
    seed_content()

