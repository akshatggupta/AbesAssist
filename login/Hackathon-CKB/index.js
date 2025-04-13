const express = require('express');
const app = express();
const port = 3000;

// Set EJS as the view engine
app.set('view engine', 'ejs');

// Middleware to parse URL-encoded data
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));


// Route for the homepage
app.get('/', (req, res) => {
  res.render('home'); // Render the homepage
});

// Route for the Attendance Calculator
app.get('/attendance', (req, res) => {
  res.render('index'); // Render the attendance calculator
});

// Route for the SGPA Calculator
app.get('/sgpa', (req, res) => {
  res.render('sgpa'); // Render the SGPA calculator
});

// Route for the Student Portals page
app.get('/portals', (req, res) => {
  res.render('portal'); // Render the portal.ejs file
});

// Demo redirect routes for each portal link
app.get('/erp-login', (req, res) => {
  res.redirect("https://erp.abes.ac.in/Login.aspx")
});

app.get('/wifi-login', (req, res) => {
  res.redirect('https://192.168.1.254:8090/');
});

app.get('/exam-form', (req, res) => {
  res.redirect("https://erp.aktu.ac.in/login.aspx")
});

app.get('/moodle', (req, res) => {
  res.send('Redirecting to Moodle...');
});

app.get('/aktu-oneview', (req, res) => {
    res.redirect("https://erp.aktu.ac.in/webpages/oneview/oneview.aspx");
});

// Route to handle attendance calculation
app.post('/calculate', (req, res) => {
  const total = parseInt(req.body.total);
  const attended = parseInt(req.body.attended);
  const target = parseFloat(req.body.target);

  const current = (attended / total) * 100;

  let required = 0;
  let requiredDays = 0;
  if (current < target) {
    required = Math.ceil(((target / 100) * total - attended) / (1 - target / 100));
    requiredDays = Math.ceil(required / 8);
  }

  res.render('result', {
    total,
    attended,
    target,
    current: current.toFixed(2),
    required,
    requiredDays,
  });
});

// Route to handle SGPA calculation
app.post('/calculate-sgpa', (req, res) => {
  const marks = req.body.marks.split(',').map(Number);
  const credits = req.body.credits.split(',').map(Number);

  if (marks.length !== credits.length) {
    return res.send('Error: The number of marks and credits must match.');
  }

  const gradePoints = marks.map(mark => {
    if (mark >= 90) return 10;
    if (mark >= 80) return 9;
    if (mark >= 70) return 8;
    if (mark >= 60) return 7;
    if (mark >= 50) return 6;
    if (mark >= 40) return 5;
    return 0;
  });

  let totalCredits = 0;
  let weightedGradePoints = 0;

  for (let i = 0; i < credits.length; i++) {
    totalCredits += credits[i];
    weightedGradePoints += gradePoints[i] * credits[i];
  }

  const sgpa = (weightedGradePoints / totalCredits).toFixed(2);

  // Render the SGPA result page
  res.render('sgpa-result', { sgpa });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
