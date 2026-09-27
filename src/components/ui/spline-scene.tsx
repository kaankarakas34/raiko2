import { lazy, Suspense } from 'react';

const Spline = lazy(() => import('@splinetool/react-spline'));

interface SplineSceneProps {
  scene: string;
  className?: string;
  onLoad?: () => void;
}

export function SplineScene({ scene, className, onLoad }: SplineSceneProps) {
  return (
    <Suspense fallback={<div className="spline-loading" aria-label="3D sahne yükleniyor"><span className="loader" /></div>}>
      <Spline scene={scene} className={className} onLoad={onLoad} />
    </Suspense>
  );
}
