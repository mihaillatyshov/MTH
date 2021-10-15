import React from 'react'

const Node = ( {node, onNodeChange} ) => {

	return (
		<div className="card node my-2 mx-2" onClick={(e) => onNodeChange(node.id)}>
			<div className="card-body">
				<h6 className="card-title">
					{node.name}
				</h6>
				<div className="card-text">
					{node.desc}
				</div>
			</div>
		</div>
	)
}

export default Node
