import React from 'react'
import Node from './Node'

const PrevNodes = ( {nodes, onNodeChange} ) => {
	return (
		<div className="col-4">
			{
				typeof nodes === 'undefined' ? (
					<div>Loading...</div>
				) : (
					nodes.map((node) => (
						<div key={node.id}>
							<Node node={node} onNodeChange={onNodeChange}/>
						</div>
					))
				)
			}
		</div>
	)
}

export default PrevNodes
