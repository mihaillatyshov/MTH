import React from 'react'

const Node = ( {node, onNodeChange} ) => {

	const handleNodeChange = (id) => {
		onNodeChange && onNodeChange(id)
	}

	return (
		<div className={`card my-2 mx-2 ${onNodeChange && 'node-pn'}`} onClick={(e) => handleNodeChange(node.id)}>
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
