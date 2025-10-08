// Academic Homepage JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // Add target="_blank" to external links
  document.querySelectorAll('a').forEach(link => {
    if (link.hostname !== window.location.hostname && !link.hasAttribute('target')) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });
});

