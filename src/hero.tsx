import { createRoot } from 'react-dom/client';
import { SplineScene } from './components/ui/spline-scene';

const mount = document.getElementById('hero-spline-root');
const hero = mount?.closest('.hero-scene');

if (mount && hero) {
  const interactive = window.matchMedia('(min-width: 761px) and (prefers-reduced-motion: no-preference)');
  let root: ReturnType<typeof createRoot> | undefined;
  let resizeObserver: ResizeObserver | undefined;
  let loadGeneration = 0;
  const updateScene = () => {
    if (interactive.matches && !root) {
      root = createRoot(mount);
      root.render(
        <SplineScene
          scene="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"
          className="spline-canvas"
          onLoad={(app) => {
            (mount as any).__splineApp = app;
            const generation = ++loadGeneration;
            const frameCamera = () => {
              const camera = app.findObjectByName('Camera 2');
              if (!camera) return;
              const aspect = mount.clientWidth / Math.max(1, mount.clientHeight);
              camera.position.y = 0;
              // Safe visible width of ~780 world units ensures the arms and gestures are never clipped by the frame
              camera.position.z = Math.round(780 / (0.414213 * Math.min(1.1, aspect)));
              app.requestRender();
            };
            frameCamera();
            window.setTimeout(() => {
              if (!interactive.matches || generation !== loadGeneration) return;
              frameCamera();
              resizeObserver?.disconnect();
              resizeObserver = new ResizeObserver(frameCamera);
              resizeObserver.observe(mount);
              hero.classList.add('scene-ready');
            }, 1000);
          }}
        />,
      );
    } else if (!interactive.matches && root) {
      loadGeneration++;
      resizeObserver?.disconnect();
      resizeObserver = undefined;
      root.unmount();
      root = undefined;
      hero.classList.remove('scene-ready');
    }
  };
  updateScene();
  interactive.addEventListener('change', updateScene);
}
