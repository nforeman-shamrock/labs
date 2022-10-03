import React, {FunctionComponent, PropsWithChildren} from 'react';
import {useDroppable} from '@dnd-kit/core';

export const Droppable: FunctionComponent<PropsWithChildren> = (props) => {
  const {isOver, setNodeRef} = useDroppable({
    id: 'droppable',
  });
  const style = {
    color: isOver ? 'green' : undefined,
  };


  return (
    <div ref={setNodeRef} style={style}>
      {props.children}
    </div>
  );
}