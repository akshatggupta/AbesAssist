


document.addEventListener('DOMContentLoaded', () => {
  const collegeLoginForm = document.getElementById('college-login-form');
  const metamaskLoginButton = document.getElementById('metamask-login');

  // Function to redirect to dashboard
  const redirectToDashboard = () => {
    window.location.href = 'Hackathon-CKB/view/home.ejs'; 
  };

  // College ID Login Form Submission
  collegeLoginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const collegeId = document.getElementById('college-id').value.trim();
    const password = document.getElementById('password').value.trim();

    // Validate College ID
    if (!collegeId.endsWith('@abes.ac.in')) {
      alert('Invalid College ID. Please enter a valid ID ending with @abes.ac.in.');
      return;
    }

    // Simulate login (replace with actual backend logic)
    console.log('Logging in with College ID:', collegeId);

    
    redirectToDashboard();
  });

  // MetaMask Login
  metamaskLoginButton.addEventListener('click', async () => {
    if (typeof window.ethereum === 'undefined') {
      alert('MetaMask is not installed. Please install MetaMask to continue.');
      return;
    }

    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const userAddress = accounts[0];
      console.log('Logged in with MetaMask address:', userAddress);

      // Redirect to dashboard after successful login
      redirectToDashboard();
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
      alert('Failed to connect to MetaMask. Please try again.');
    }
  });
});