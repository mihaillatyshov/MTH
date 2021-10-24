import React from 'react'
import Node from './Node'

const PrevNodes = ( {nodes, onNodeChange} ) => {
	return (
		<div className="col">
			{
				nodes.map((node) => (
					<div key={node.id}>
						<Node node={node} onNodeChange={onNodeChange}/>
					</div>
				))
			}
		</div>
	)
}

export default PrevNodes
