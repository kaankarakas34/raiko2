import { createRoot } from 'react-dom/client';
import { SplineScene } from './components/ui/spline-scene';

const mount = document.getElementById('hero-spline-root');
const hero = mount?.closest('.hero-scene');

if (mount && hero) {
  const interactive = window.matchMedia('(min-width: 761px) and (prefers-reduced-motion: no-preference)');
  let root: ReturnType<typeof createRoot> | undefined;
  const updateScene = () => {
    if (interactive.matches && !root) {
      root = createRoot(mount);
      root.render(
        <SplineScene
          scene="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"
          className="spline-canvas"
          onLoad={() => hero.classList.add('scene-ready')}
        />,
      );
    } else if (!interactive.matches && root) {
      root.unmount();
      root = undefined;
      hero.classList.remove('scene-ready');
    }
  };
  updateScene();
  interactive.addEventListener('change', updateScene);
}
