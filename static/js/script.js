document.addEventListener("DOMContentLoaded", function () {
  // Mobile menu
  const toggle = document.getElementById("menu-toggle");
  const navLinks = document.getElementById("nav-links");

  if (toggle && navLinks) {
    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      navLinks.classList.toggle("active");
      toggle.classList.toggle("open");
    });
  }

  // Dropdowns
  const dropdowns = document.querySelectorAll(".dropdown");
  dropdowns.forEach((dropdown) => {
    const link = dropdown.querySelector("a");
    if (link) {
      link.addEventListener("click", function (e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          e.stopPropagation();
          dropdown.classList.toggle("open");

          dropdowns.forEach((item) => {
            if (item !== dropdown) {
              item.classList.remove("open");
            }
          });
        }
      });
    }
  });

  document.addEventListener("click", () => {
    dropdowns.forEach((dropdown) => dropdown.classList.remove("open"));
  });

  // Animate feature cards
  const featureCards = document.querySelectorAll('.feature-card');
  const featuresSection = document.querySelector('.features');
  if (featuresSection) {
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          featureCards.forEach((card, index) => {
            setTimeout(() => {
              card.classList.add('animate');
            }, index * 200);
          });
          observer.unobserve(featuresSection);
        }
      });
    }, { threshold: 0.4 });
    observer.observe(featuresSection);
  }

  // Animate palette colors
  const paletteSection = document.querySelector('.palette-section');
  const paletteColors = document.querySelectorAll('.palette-color');
  if (paletteSection && paletteColors.length > 0) {
    const paletteObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          paletteColors.forEach((color, index) => {
            setTimeout(() => {
              color.classList.add('animate');
              color.style.animation = 'pulse 0.8s ease';
            }, index * 100);
          });
          observer.unobserve(paletteSection);
        }
      });
    }, { threshold: 0.4 });
    paletteObserver.observe(paletteSection);
  }

  // Counters
  const counters = document.querySelectorAll('.counter');

  const startCounting = (counter) => {
    counter.innerText = '0';
    const updateCounter = () => {
      const target = +counter.getAttribute('data-target');
      const current = +counter.innerText;
      const increment = target / 100;

      if (current < target) {
        counter.innerText = `${Math.ceil(current + increment)}`;
        setTimeout(updateCounter, 20);
      } else {
        counter.innerText = target;
      }
    };
    updateCounter();
  };

  const counterOptions = {
    threshold: 0.5
  };

  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counters = entry.target.querySelectorAll('.counter');
        counters.forEach(counter => startCounting(counter));
        observer.unobserve(entry.target);
      }
    });
  }, counterOptions);

  const featuresCounterSection = document.querySelector('.features-section');
  if (featuresCounterSection) {
    counterObserver.observe(featuresCounterSection);
  }

  // Animate contact page elements
  const elements = document.querySelectorAll('.contact-info, .contact-form, .intro, .contact-section h1');
  elements.forEach((el, index) => {
    el.classList.add('hidden');
    setTimeout(() => {
      el.classList.add('show');
    }, index * 200);
  });

});
