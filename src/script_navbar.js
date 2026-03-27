const NAVBAR = document.querySelector('.contenedor-header');
const NAV = document.querySelector('nav');
const NAV_TRIGGER = document.querySelector('.nav-responsive');
const NAV_LINKS = document.querySelector('nav#nav ul');

let lastScrollY = 0;
let ticking = false;

function updateNavbar() {
    const currentScrollY = window.scrollY;
    
    if (currentScrollY > 100) {
        NAVBAR.classList.add('scrolled');
    } else {
        NAVBAR.classList.remove('scrolled');
    }
    
    lastScrollY = currentScrollY;
    ticking = false;
}

window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(updateNavbar);
        ticking = true;
    }
});

if (NAV_TRIGGER) {
    NAV_TRIGGER.addEventListener('click', () => {
        NAV_LINKS.classList.toggle('show');
        const icon = NAV_TRIGGER.querySelector('i');
        if (NAV_LINKS.classList.contains('show')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });
}

document.querySelectorAll('nav#nav ul li a').forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
            NAV_LINKS.classList.remove('show');
            if (NAV_TRIGGER) {
                const icon = NAV_TRIGGER.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        }
    });
});

if (window.innerWidth > 768) {
    NAV.style.display = 'flex';
} else {
    NAV.style.display = 'none';
}

window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        NAV.style.display = 'flex';
        NAV_LINKS.classList.remove('show');
        if (NAV_TRIGGER) {
            const icon = NAV_TRIGGER.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    } else {
        NAV.style.display = 'none';
    }
});

const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav#nav ul li a');

function highlightNavLink() {
    const scrollY = window.scrollY;
    
    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 150;
        const sectionId = section.getAttribute('id');
        
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

window.addEventListener('scroll', highlightNavLink);
highlightNavLink();
