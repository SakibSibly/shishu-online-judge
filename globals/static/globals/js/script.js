document.addEventListener('DOMContentLoaded', function() {
    var textarea = document.getElementById('code');

    textarea.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            e.preventDefault();

            var start = this.selectionStart;
            var end = this.selectionEnd;

            this.value = this.value.substring(0, start) + '\t' + this.value.substring(end);

            this.selectionStart = this.selectionEnd = start + 1;
        }
    });
});


document.addEventListener('DOMContentLoaded', function () 
{
    const nav = document.querySelector('nav.distance');
    const animation = nav.querySelector('.animation');
    const links = nav.querySelectorAll('a');

    function updateAnimationPosition() 
    {
        const activeLink = nav.querySelector('a.active');

        if (activeLink) {
            const left = activeLink.offsetLeft;
            const width = activeLink.offsetWidth;
            animation.style.left = `${left}px`;
            animation.style.width = `${width}px`;
        }

    }

    function setActiveLink(link) 
    {
        links.forEach(link => link.classList.remove('active'));
        link.classList.add('active');
        updateAnimationPosition();
        localStorage.setItem('activeLink', link.href);
        
    }

    links.forEach(link => {

        link.addEventListener('click', function () {
            setActiveLink(this);
        });

        link.addEventListener('mouseover', function () 
        {
            const left = this.offsetLeft;
            const width = this.offsetWidth;
            animation.style.left = `${left}px`;
            animation.style.width = `${width}px`;
        });

        link.addEventListener('mouseout', function () {
            updateAnimationPosition();
        });

    });

    
    const activeLinkHref = localStorage.getItem('activeLink');
    
    if (activeLinkHref) 
    {
        const activeLink = Array.from(links).find(link => link.href === activeLinkHref);

        if (activeLink) {
            setActiveLink(activeLink);
        }
    } 
    
    
    else 
    {
        const defaultActiveLink = nav.querySelector('a');

        if (defaultActiveLink) {
            setActiveLink(defaultActiveLink);
        }
    }

    updateAnimationPosition();

});