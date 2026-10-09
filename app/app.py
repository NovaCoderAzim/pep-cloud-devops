
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mohammed Azim | Portfolio</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html {
                scroll-behavior: smooth;
            }

            body {
                font-family: Arial, sans-serif;
                background: #0b1120;
                color: #e2e8f0;
                line-height: 1.7;
            }

            nav {
                padding: 20px 8%;
                background: #111827;
                border-bottom: 1px solid #263247;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 15px;
            }

            .logo {
                color: #38bdf8;
                font-size: 24px;
                font-weight: bold;
            }

            nav a {
                color: #cbd5e1;
                text-decoration: none;
                margin-left: 18px;
                font-size: 14px;
            }

            nav a:hover {
                color: #38bdf8;
            }

            section {
                padding: 65px 8%;
            }

            .hero {
                min-height: 75vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: flex-start;
            }

            .tag {
                color: #38bdf8;
                font-size: 13px;
                letter-spacing: 3px;
                margin-bottom: 18px;
            }

            h1 {
                font-size: clamp(38px, 6vw, 64px);
                line-height: 1.2;
                margin-bottom: 20px;
            }

            h1 span {
                color: #38bdf8;
            }

            .hero p {
                color: #94a3b8;
                max-width: 650px;
                font-size: 17px;
                margin-bottom: 28px;
            }

            .btn {
                display: inline-block;
                padding: 11px 20px;
                border-radius: 6px;
                background: #38bdf8;
                color: #07111f;
                text-decoration: none;
                font-weight: bold;
                margin-right: 10px;
                margin-bottom: 10px;
            }

            .btn.outline {
                color: #38bdf8;
                background: transparent;
                border: 1px solid #38bdf8;
            }

            h2 {
                font-size: 30px;
                margin-bottom: 10px;
            }

            .subtitle {
                color: #94a3b8;
                margin-bottom: 28px;
            }

            .card {
                background: #111c30;
                border: 1px solid #263247;
                border-radius: 10px;
                padding: 24px;
            }

            .card h3 {
                margin-bottom: 12px;
                color: #f1f5f9;
            }

            .card p {
                color: #aab6c8;
            }

            .grid {
                display: grid;
                grid-template-columns:
                    repeat(auto-fit, minmax(230px, 1fr));
                gap: 20px;
            }

            .skills {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 18px;
            }

            .skills span {
                background: #17263c;
                border: 1px solid #29445f;
                border-radius: 5px;
                padding: 6px 12px;
                color: #7dd3fc;
                font-size: 13px;
            }

            .project-link {
                display: inline-block;
                margin-top: 15px;
                color: #38bdf8;
                text-decoration: none;
            }

            .project-link:hover {
                text-decoration: underline;
            }

            footer {
                padding: 25px;
                text-align: center;
                border-top: 1px solid #263247;
                color: #64748b;
                font-size: 14px;
            }

            @media (max-width: 600px) {
                nav {
                    flex-direction: column;
                }

                nav a {
                    margin: 0 6px;
                }

                section {
                    padding: 45px 6%;
                }
            }
        </style>
    </head>

    <body>

        <nav>
            <div class="logo">Azim.</div>
            <div>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </div>
        </nav>

        <section class="hero">
            <div class="tag">COMPUTER SCIENCE ENGINEERING</div>

            <h1>Hi, I'm<br><span>Mohammed Azim</span></h1>

            <p>
                A third-year CSE student passionate about Cloud Computing,
                DevOps, and Software Development. I enjoy learning new
                technologies and building practical projects.
            </p>

            <div>
                <a href="#projects" class="btn">Explore My Projects</a>
                <a href="#contact" class="btn outline">Get In Touch</a>
            </div>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p class="subtitle">A little about my journey.</p>

            <div class="card">
                <p>
                    I'm a Computer Science Engineering student developing
                    my skills in cloud infrastructure, programming, and
                    automation. I have been exploring AWS, Docker, Jenkins,
                    and Terraform through hands-on projects. I'm focused on
                    learning, improving my technical skills, and gaining
                    practical industry experience.
                </p>
            </div>
        </section>

        <section id="skills">
            <h2>Skills & Technologies</h2>
            <p class="subtitle">Tools and technologies I'm learning.</p>

            <div class="grid">
                <div class="card">
                    <h3>☁️ Cloud Computing</h3>
                    <p>Cloud infrastructure and deployment.</p>
                    <div class="skills">
                        <span>AWS EC2</span>
                        <span>VPC</span>
                        <span>IAM</span>
                    </div>
                </div>

                <div class="card">
                    <h3>⚙️ DevOps</h3>
                    <p>Automation and infrastructure management.</p>
                    <div class="skills">
                        <span>Docker</span>
                        <span>Jenkins</span>
                        <span>Terraform</span>
                        <span>Git</span>
                        <span>GitHub</span>
                    </div>
                </div>

                <div class="card">
                    <h3>💻 Programming</h3>
                    <p>Programming and web development fundamentals.</p>
                    <div class="skills">
                        <span>Python</span>
                        <span>Java</span>
                        <span>HTML</span>
                        <span>CSS</span>
                    </div>
                </div>
            </div>
        </section>

        <section id="projects">
            <h2>Featured Projects</h2>
            <p class="subtitle">Things I've been building and learning.</p>

            <div class="grid">
                <div class="card">
                    <h3>Cloud & DevOps CI/CD</h3>
                    <p>
                        A web application built with Flask, containerized
                        using Docker, and deployed to AWS EC2 using a
                        Jenkins Freestyle job.
                    </p>
                    <a class="project-link"
                       href="https://github.com/NovaCoderAzim/pep-cloud-devops"
                       target="_blank"
                       rel="noopener noreferrer">
                        View Project ↗
                    </a>
                </div>

                <div class="card">
                    <h3>AWS Infrastructure with Terraform</h3>
                    <p>
                        Provisioning AWS networking resources and EC2
                        instances using Infrastructure as Code.
                    </p>
                    <a class="project-link"
                       href="https://github.com/NovaCoderAzim/pep-cloud-devops"
                       target="_blank"
                       rel="noopener noreferrer">
                        View Project ↗
                    </a>
                </div>

                <div class="card">
                    <h3>What's Next?</h3>
                    <p>
                        Exploring more cloud technologies and developing
                        new projects to strengthen my technical skills.
                    </p>
                </div>
            </div>
        </section>

        <section id="contact">
            <h2>Let's Connect</h2>
            <p class="subtitle">
                Feel free to explore my work or connect with me.
            </p>

            <div class="card">
                <p>
                    I'm interested in technology, continuous learning,
                    collaboration, and new opportunities.
                </p>

                <br>

                <a class="btn"
                   href="https://github.com/NovaCoderAzim"
                   target="_blank"
                   rel="noopener noreferrer">
                    GitHub
                </a>

                <a class="btn outline"
                   href="https://www.linkedin.com/in/mohammed-azim-j-029477383/"
                   target="_blank"
                   rel="noopener noreferrer">
                    LinkedIn
                </a>
            </div>
        </section>

        <footer>
            © 2026 Mohammed Azim | Built with Flask, HTML & CSS
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
